"""Crawl discovered application pages, capture screenshots, and collect UI evidence.

The crawler never intentionally selects Save, Submit, Delete, Remove, Approve,
or other state changing actions. It captures list pages and safely opens common
Create, Edit, View, Show, and Details interfaces when they are available.
"""

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urljoin

from playwright.sync_api import Page, sync_playwright

CREATE_RE = re.compile(
    r"create|add new|new record|new item|add employee|register",
    re.I,
)

EDIT_RE = re.compile(
    r"^\s*(edit|update|modify)\s*$",
    re.I,
)

SHOW_RE = re.compile(
    r"^\s*(view|show|details|open)\s*$",
    re.I,
)

RISKY_RE = re.compile(
    r"save|submit|delete|remove|approve|reject|confirm|pay|publish|send|archive",
    re.I,
)


def slug(text: str) -> str:
    return (
        re.sub(
            r"[^a-z0-9]+",
            "_",
            text.strip().lower(),
        ).strip("_")
        or "page"
    )


def visible_text(
    locator,
    timeout: int = 800,
) -> str:
    try:
        if locator.is_visible(
            timeout=timeout
        ):
            return locator.inner_text(
                timeout=timeout
            ).strip()

    except Exception:
        pass

    return ""


def extract_ui_evidence(
    page: Page,
) -> dict:
    script = r"""
    () => {
      const isVisible = (el) => {
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();

        return style.visibility !== 'hidden' &&
               style.display !== 'none' &&
               rect.width > 0 &&
               rect.height > 0;
      };

      const clean = (value) =>
        (value || '')
          .replace(/\s+/g, ' ')
          .trim();

      const textOf = (el) =>
        clean(
          el.innerText ||
          el.textContent ||
          ''
        );

      const unique = (items, keyFn) => {
        const seen = new Set();

        return items.filter((item) => {
          const key = keyFn(item);

          if (!key || seen.has(key)) {
            return false;
          }

          seen.add(key);
          return true;
        });
      };

      const associatedLabel = (el) => {
        if (el.id) {
          const label = document.querySelector(
            `label[for="${CSS.escape(el.id)}"]`
          );

          if (label) {
            return textOf(label);
          }
        }

        const parentLabel = el.closest('label');

        if (parentLabel) {
          return textOf(parentLabel);
        }

        const aria = el.getAttribute(
          'aria-label'
        );

        if (aria) {
          return clean(aria);
        }

        const labelledBy = el.getAttribute(
          'aria-labelledby'
        );

        if (labelledBy) {
          return labelledBy
            .split(/\s+/)
            .map((id) => {
              const node =
                document.getElementById(id);

              return node
                ? textOf(node)
                : '';
            })
            .filter(Boolean)
            .join(' ');
        }

        return '';
      };

      const headings = [
        ...document.querySelectorAll(
          'h1, h2, h3'
        )
      ]
        .filter(isVisible)
        .map(textOf)
        .filter(Boolean)
        .slice(0, 20);

      const breadcrumbSelectors = [
        '[aria-label*="breadcrumb" i]',
        '.breadcrumb',
        'nav.breadcrumb',
        '[class*="breadcrumb" i]'
      ];

      const breadcrumbs = unique(
        breadcrumbSelectors
          .flatMap((selector) =>
            [
              ...document.querySelectorAll(
                selector
              )
            ]
              .filter(isVisible)
              .map(textOf)
          )
          .filter(Boolean),
        (value) => value
      ).slice(0, 10);

      const controls = unique(
        [
          ...document.querySelectorAll(
            'button, a, [role="button"]'
          )
        ]
          .filter(isVisible)
          .map((el) => ({
            text: textOf(el),
            aria_label: clean(
              el.getAttribute('aria-label')
            ),
            title: clean(
              el.getAttribute('title')
            ),
            tag: el.tagName.toLowerCase(),
            href: clean(
              el.getAttribute('href')
            ),
            disabled: Boolean(
              el.disabled ||
              el.getAttribute(
                'aria-disabled'
              ) === 'true'
            )
          }))
          .filter(
            (item) =>
              item.text ||
              item.aria_label ||
              item.title
          ),
        (item) =>
          `${item.text}|${item.aria_label}|${item.title}|${item.href}`
      ).slice(0, 120);

      const fields = unique(
        [
          ...document.querySelectorAll(
            'input, textarea, select'
          )
        ]
          .filter(isVisible)
          .map((el) => ({
            label: associatedLabel(el),
            type:
              clean(
                el.getAttribute('type')
              ) ||
              el.tagName.toLowerCase(),
            name: clean(
              el.getAttribute('name')
            ),
            id: clean(el.id),
            placeholder: clean(
              el.getAttribute(
                'placeholder'
              )
            ),
            required: Boolean(
              el.required ||
              el.getAttribute(
                'aria-required'
              ) === 'true'
            ),
            disabled: Boolean(
              el.disabled
            ),
            options:
              el.tagName.toLowerCase() ===
              'select'
                ? [...el.options]
                    .map((option) =>
                      clean(
                        option.textContent
                      )
                    )
                    .filter(Boolean)
                    .slice(0, 30)
                : []
          })),
        (item) =>
          `${item.label}|${item.name}|${item.id}|${item.placeholder}`
      ).slice(0, 120);

      const tables = [
        ...document.querySelectorAll(
          'table'
        )
      ]
        .filter(isVisible)
        .slice(0, 20)
        .map((table, index) => ({
          index,
          headers: [
            ...table.querySelectorAll(
              'thead th, tr:first-child th, tr:first-child td'
            )
          ]
            .map(textOf)
            .filter(Boolean)
            .slice(0, 40),
          visible_row_count: [
            ...table.querySelectorAll(
              'tbody tr'
            )
          ].filter(isVisible).length
        }));

      const tabs = unique(
        [
          ...document.querySelectorAll(
            '[role="tab"], .nav-tabs a, [class*="tab" i] button'
          )
        ]
          .filter(isVisible)
          .map(textOf)
          .filter(Boolean),
        (value) => value
      ).slice(0, 40);

      const messages = unique(
        [
          ...document.querySelectorAll(
            '[role="alert"], .alert, .error, .warning, .success, [class*="toast" i]'
          )
        ]
          .filter(isVisible)
          .map(textOf)
          .filter(Boolean),
        (value) => value
      ).slice(0, 30);

      const forms = [
        ...document.querySelectorAll(
          'form'
        )
      ]
        .filter(isVisible)
        .slice(0, 20)
        .map((form, index) => ({
          index,
          action: clean(
            form.getAttribute('action')
          ),
          method: clean(
            form.getAttribute('method')
          ),
          field_count:
            form.querySelectorAll(
              'input, textarea, select'
            ).length
        }));

      return {
        document_title: clean(
          document.title
        ),
        url: window.location.href,
        headings,
        breadcrumbs,
        controls,
        fields,
        tables,
        tabs,
        messages,
        forms,
        body_text_preview: clean(
          document.body.innerText
        ).slice(0, 5000)
      };
    }
    """

    try:
        return page.evaluate(
            script
        )

    except Exception as exc:
        return {
            "url": page.url,
            "evidence_error": str(exc),
        }


def try_close(
    page: Page,
) -> None:
    selectors = [
        'button:has-text("Cancel")',
        'button:has-text("Close")',
        '[aria-label="close" i]',
        '[aria-label="dismiss" i]',
        'button[title="Close" i]',
    ]

    for selector in selectors:
        try:
            button = page.locator(
                selector
            ).first

            if button.is_visible(
                timeout=700
            ):
                button.click(
                    timeout=2000
                )

                page.wait_for_timeout(
                    350
                )

                return

        except Exception:
            pass

    try:
        page.keyboard.press(
            "Escape"
        )

        page.wait_for_timeout(
            350
        )

    except Exception:
        pass


def safe_click(
    locator,
) -> bool:
    try:
        text = " ".join(
            value
            for value in [
                visible_text(locator),
                locator.get_attribute(
                    "aria-label"
                )
                or "",
                locator.get_attribute(
                    "title"
                )
                or "",
            ]
            if value
        )

        if RISKY_RE.search(text):
            return False

        if not locator.is_visible(
            timeout=1500
        ):
            return False

        locator.click(
            timeout=3000
        )

        return True

    except Exception:
        return False


def capture_state(
    page: Page,
    folder: Path,
    page_slug: str,
    state_name: str,
) -> dict:
    if state_name == "screen":
        screenshot_name = (
            f"{page_slug}.png"
        )

    else:
        screenshot_name = (
            f"{page_slug}_{state_name}.png"
        )

    screenshot_path = (
        folder / screenshot_name
    )

    page.screenshot(
        path=str(screenshot_path),
        full_page=True,
        timeout=20000,
    )

    return {
        "state": state_name,
        "screenshot": screenshot_path.name,
        "evidence": extract_ui_evidence(
            page
        ),
    }


def capture_action(
    page: Page,
    folder: Path,
    page_slug: str,
    state_name: str,
    click_locator,
) -> dict | None:
    original_url = page.url

    if not safe_click(
        click_locator
    ):
        return None

    try:
        page.wait_for_timeout(
            1200
        )

        try:
            page.wait_for_load_state(
                "networkidle",
                timeout=5000,
            )

        except Exception:
            pass

        result = capture_state(
            page,
            folder,
            page_slug,
            state_name,
        )

    except Exception:
        result = None

    if page.url != original_url:
        try:
            page.go_back(
                timeout=10000
            )

            page.wait_for_timeout(
                700
            )

        except Exception:
            pass

    else:
        try_close(
            page
        )

    return result


def find_action_locator(
    page: Page,
    action: str,
):
    if action == "create":
        pattern = CREATE_RE

    elif action == "edit":
        pattern = EDIT_RE

    else:
        pattern = SHOW_RE

    try:
        locator = page.locator(
            'button, a, [role="button"]'
        ).filter(
            has_text=pattern
        ).first

        if locator.is_visible(
            timeout=700
        ):
            return locator

    except Exception:
        pass

    icon_selectors = {
        "create": [
            '[aria-label*="add" i]',
            '[title*="add" i]',
            '[aria-label*="create" i]',
            '[title*="create" i]',
            'svg[data-testid*="Add" i]',
        ],
        "edit": [
            '[aria-label*="edit" i]',
            '[title*="edit" i]',
            'svg[data-testid*="Edit" i]',
        ],
        "show": [
            '[aria-label*="view" i]',
            '[title*="view" i]',
            '[aria-label*="details" i]',
            '[title*="details" i]',
            'svg[data-testid*="Visibility" i]',
        ],
    }

    for selector in icon_selectors[
        action
    ]:
        try:
            target = page.locator(
                selector
            ).first

            candidate = target.locator(
                "xpath=ancestor-or-self::button | ancestor-or-self::a"
            ).first

            if candidate.is_visible(
                timeout=700
            ):
                return candidate

        except Exception:
            pass

    return None


def crawl_module(
    page: Page,
    base: str,
    module: str,
    entries: list,
    output_root: Path,
) -> list[dict]:
    folder = (
        output_root / slug(module)
    )

    folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    page_records = []

    for entry in entries:
        text = (
            entry.get("text")
            or entry.get("href")
            or "Page"
        )

        href = (
            entry.get("href")
            or ""
        )

        page_slug = (
            slug(text)
            or slug(href)
        )

        url = urljoin(
            base,
            href,
        )

        record = {
            "module": module,
            "page_key": page_slug,
            "navigation_text": text,
            "href": href,
            "url": url,
            "states": [],
        }

        try:
            page.goto(
                url,
                timeout=30000,
            )

            try:
                page.wait_for_load_state(
                    "networkidle",
                    timeout=10000,
                )

            except Exception:
                pass

            page.wait_for_timeout(
                1200
            )

            record["states"].append(
                capture_state(
                    page,
                    folder,
                    page_slug,
                    "screen",
                )
            )

            print(
                f"OK {module}/{page_slug}"
            )

        except Exception as exc:
            record["error"] = str(exc)

            page_records.append(
                record
            )

            print(
                f"FAIL {module}/{page_slug}: {exc}"
            )

            continue

        for action in [
            "create",
            "edit",
            "show",
        ]:
            locator = find_action_locator(
                page,
                action,
            )

            if locator is None:
                continue

            state = capture_action(
                page,
                folder,
                page_slug,
                action,
                locator,
            )

            if state:
                record["states"].append(
                    state
                )

                print(
                    f"OK {module}/{page_slug}_{action}"
                )

        page_records.append(
            record
        )

    return page_records


def run(
    project_dir: Path,
    modules=None,
) -> None:
    discovery_path = (
        project_dir
        / "discovery.json"
    )

    if not discovery_path.is_file():
        raise RuntimeError(
            f"Discovery file not found: {discovery_path}"
        )

    discovery = json.loads(
        discovery_path.read_text(
            encoding="utf-8"
        )
    )

    base = discovery[
        "base_url"
    ]

    output_root = (
        project_dir
        / "screenshots"
    )

    output_root.mkdir(
        parents=True,
        exist_ok=True,
    )

    selected_modules = (
        modules
        or [
            name
            for name in discovery
            if name != "base_url"
        ]
    )

    complete_evidence = {
        "base_url": base,
        "project": project_dir.name,
        "modules": {},
    }

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True
        )

        context = browser.new_context(
            storage_state=str(
                project_dir
                / "auth_state.json"
            ),
            viewport={
                "width": 1920,
                "height": 1000,
            },
        )

        page = context.new_page()

        for module in selected_modules:
            entries = discovery.get(
                module,
                {},
            ).get(
                "links",
                [],
            )

            if not entries:
                print(
                    f"SKIP {module}: no pages"
                )

                continue

            complete_evidence[
                "modules"
            ][module] = crawl_module(
                page,
                base,
                module,
                entries,
                output_root,
            )

        context.close()
        browser.close()

    evidence_path = (
        project_dir
        / "ui_evidence.json"
    )

    evidence_path.write_text(
        json.dumps(
            complete_evidence,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        f"Wrote UI evidence: {evidence_path}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__
    )

    parser.add_argument(
        "project_dir",
        help="Project folder path",
    )

    parser.add_argument(
        "modules",
        nargs="*",
        help="Optional module names",
    )

    args = parser.parse_args()

    run(
        Path(args.project_dir),
        args.modules or None,
    )


if __name__ == "__main__":
    try:
        main()

    except RuntimeError as exc:
        print(
            f"ERROR: {exc}"
        )

        raise SystemExit(1)