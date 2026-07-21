"""Crawl every PeopleDesk page from discovery.json, screenshot the list view, and
best-effort screenshot Create/Edit/Show modals (never Save/Submit/Delete)."""
import json
import re
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
BASE = "https://app.peopledesk.io"
DISCOVERY = json.loads((HERE / "discovery.json").read_text(encoding="utf-8"))

CREATE_RE = re.compile(r"create|add new", re.I)
EDIT_RE = re.compile(r"^\s*edit\s*$", re.I)
SHOW_RE = re.compile(r"^\s*(view|show|details)\s*$", re.I)


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.strip().lower()).strip("_")


def try_close(pg):
    for sel in ['button:has-text("Cancel")', 'button:has-text("Close")', '[aria-label="close"]']:
        try:
            btn = pg.locator(sel).first
            if btn.is_visible(timeout=1000):
                btn.click(timeout=2000)
                pg.wait_for_timeout(400)
                return
        except Exception:
            pass
    try:
        pg.keyboard.press("Escape")
        pg.wait_for_timeout(400)
    except Exception:
        pass


def capture_action(pg, folder: Path, page_slug: str, suffix: str, click_locator):
    try:
        if not click_locator.is_visible(timeout=1500):
            return False
        click_locator.click(timeout=3000)
        pg.wait_for_timeout(1500)
        pg.screenshot(path=str(folder / f"{page_slug}_{suffix}.png"), full_page=True, timeout=15000)
        try_close(pg)
        return True
    except Exception:
        return False


def crawl_module(pg, module: str, entries: list, out_root: Path):
    folder = out_root / slug(module)
    folder.mkdir(parents=True, exist_ok=True)
    for entry in entries:
        text, href = entry["text"], entry["href"]
        page_slug = slug(text) or slug(href)
        url = BASE + href
        try:
            pg.goto(url, timeout=30000)
            try:
                pg.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                pass
            pg.wait_for_timeout(1500)
            pg.screenshot(path=str(folder / f"{page_slug}.png"), full_page=True, timeout=15000)
            print(f"OK {module}/{page_slug}")
        except Exception as e:
            print(f"FAIL {module}/{page_slug}: {e}")
            continue

        # Best-effort Create button (matched via a "+"/AddOutlinedIcon svg first, then text)
        try:
            create_btn = pg.locator("button, a").filter(
                has=pg.locator('svg[data-testid="AddOutlinedIcon"]')
            ).first
            ok = capture_action(pg, folder, page_slug, "create", create_btn)
            if not ok:
                create_btn = pg.locator("button, a").filter(has_text=CREATE_RE).first
                ok = capture_action(pg, folder, page_slug, "create", create_btn)
            if ok:
                print(f"OK {module}/{page_slug}_create")
        except Exception:
            pass

        # Best-effort Edit button (only plain labeled buttons/links, not icon-only virtualized actions)
        try:
            edit_btn = pg.locator("button, a").filter(has_text=EDIT_RE).first
            if capture_action(pg, folder, page_slug, "edit", edit_btn):
                print(f"OK {module}/{page_slug}_edit")
        except Exception:
            pass

        # Best-effort Show/View button (same constraint as Edit)
        try:
            show_btn = pg.locator("button, a").filter(has_text=SHOW_RE).first
            if capture_action(pg, folder, page_slug, "show", show_btn):
                print(f"OK {module}/{page_slug}_show")
        except Exception:
            pass


def main():
    modules = sys.argv[1:] or [m for m in DISCOVERY if m != "Recruitment"]
    out_root = HERE / "screenshots"
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        ctx = b.new_context(storage_state=str(HERE / "auth_state.json"), viewport={"width": 1920, "height": 1000})
        pg = ctx.new_page()
        for module in modules:
            entries = DISCOVERY.get(module, {}).get("links", [])
            if not entries:
                print(f"SKIP {module}: no pages")
                continue
            crawl_module(pg, module, entries, out_root)
        ctx.close()
        b.close()


if __name__ == "__main__":
    main()
