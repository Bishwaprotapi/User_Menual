"""Generate task structured manual sections from screenshots and UI evidence."""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import errors, types
from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))

import build_pdf
import debug_logger

DEFAULT_MODEL = (
    "gemini-3.1-flash-lite"
)

PAGES_PER_BATCH = 8

MAX_RETRIES = 8

DEFAULT_RETRY_DELAY = 20.0

BATCH_PAUSE_SECONDS = 3.0

VARIANT_RE = re.compile(
    r"_(create|edit|show)$"
)

IMAGE_SUFFIXES = {
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
}

PROMPT = """You are a senior technical writer and software product analyst.

Software: {software_name}
Purpose: {purpose}
Audience: {audience}
Module: {module_name}

Create task based user manual data from the supplied screenshots and UI evidence.
Use only information visible in the screenshots or present in the evidence.
Do not invent buttons, fields, permissions, results, or business rules.

Return valid JSON with this exact shape:
{{
  "pages": [
    {{
      "page_key": "the supplied page key",
      "page_name": "clear user facing page name",
      "summary": "what the page is used for",
      "route": "route or URL when available",
      "roles": ["roles only when supported by evidence"],
      "tasks": [
        {{
          "task_name": "one clear user goal",
          "action_type": "view, create, edit, search, filter, approve, export, configure, or other",
          "purpose": "why a user performs this task",
          "prerequisites": ["facts that must be true before starting"],
          "steps": ["ordered actions written as direct instructions"],
          "fields": [
            {{
              "name": "visible field or column name",
              "description": "what the field appears to contain",
              "required": false
            }}
          ],
          "expected_result": "observable result supported by the interface",
          "warnings": ["validation or safety warnings supported by evidence"],
          "keywords": ["synonyms and phrases users may ask"]
        }}
      ]
    }}
  ]
}}

Rules:
1. Create at least one task for every page.
2. Separate Create, Edit, View, Search, Filter, and other goals when evidence supports them.
3. Steps must begin from the module or page and must not claim that Save or Submit was tested.
4. When a final result is not visible, write that the user should verify the record or status after completing the form.
5. Include visible button labels, field labels, table columns, tabs, and form titles.
6. Keep each task self contained so it can be retrieved as one knowledge chunk.
7. Keep page_key exactly equal to one supplied page key.
8. Return JSON only.

Pages and evidence:
{page_payload}
"""


def slug(
    text: str,
) -> str:
    return (
        re.sub(
            r"[^a-z0-9]+",
            "_",
            text.strip().lower(),
        ).strip("_")
        or "section"
    )


def group_by_page(
    files: list[Path],
) -> dict[str, list[Path]]:
    groups = {}

    for file_path in sorted(
        files
    ):
        base = VARIANT_RE.sub(
            "",
            file_path.stem,
        )

        groups.setdefault(
            base,
            [],
        ).append(
            file_path
        )

    return groups


def chunk_items(
    items: list,
    size: int,
):
    for index in range(
        0,
        len(items),
        size,
    ):
        yield items[
            index:
            index + size
        ]


def parse_retry_delay(
    exc: errors.APIError,
) -> float:
    details = (
        exc.details
        if isinstance(exc.details, dict)
        else {}
    )

    for entry in details.get(
        "error",
        details,
    ).get(
        "details",
        [],
    ):
        delay = entry.get("retryDelay")

        if delay:
            match = re.match(
                r"([\d.]+)",
                delay,
            )

            if match:
                return float(match.group(1))

    return DEFAULT_RETRY_DELAY


def generate_content_with_retry(
    client,
    model: str,
    contents: list,
    config,
):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return client.models.generate_content(
                model=model,
                contents=contents,
                config=config,
            )

        except errors.ClientError as exc:
            if exc.code != 429 or attempt == MAX_RETRIES:
                raise

            delay = parse_retry_delay(exc) + 2.0

            print(
                (
                    f"  Rate limited (attempt {attempt}/{MAX_RETRIES}), "
                    f"waiting {delay:.0f}s..."
                )
            )

            time.sleep(delay)

        except errors.ServerError as exc:
            if attempt == MAX_RETRIES:
                raise

            delay = min(
                60.0,
                DEFAULT_RETRY_DELAY * attempt,
            )

            print(
                (
                    f"  Server error (attempt {attempt}/{MAX_RETRIES}), "
                    f"waiting {delay:.0f}s..."
                )
            )

            time.sleep(delay)

    raise RuntimeError(
        "generate_content_with_retry: exhausted retries"
    )


def load_evidence(
    project_dir: Path,
) -> dict:
    path = (
        project_dir
        / "ui_evidence.json"
    )

    if not path.is_file():
        return {
            "modules": {}
        }

    return json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )


def module_evidence_map(
    all_evidence: dict,
    module_name: str,
) -> dict:
    records = all_evidence.get(
        "modules",
        {},
    ).get(
        module_name,
        [],
    )

    return {
        record.get(
            "page_key",
            "",
        ): record
        for record in records
    }


def clean_json_text(
    text: str,
) -> str:
    cleaned = text.strip()

    if cleaned.startswith(
        "```"
    ):
        cleaned = re.sub(
            r"^```(?:json)?\s*",
            "",
            cleaned,
        )

        cleaned = re.sub(
            r"\s*```$",
            "",
            cleaned,
        )

    return cleaned.strip()


def parse_response_json(
    text: str,
) -> dict:
    cleaned = clean_json_text(
        text
    )

    try:
        return json.loads(
            cleaned
        )

    except json.JSONDecodeError:
        start = cleaned.find(
            "{"
        )

        end = cleaned.rfind(
            "}"
        )

        if (
            start >= 0
            and end > start
        ):
            return json.loads(
                cleaned[
                    start:
                    end + 1
                ]
            )

        raise


def image_markdown(
    page_key: str,
    files: list[Path],
    project_dir: Path,
) -> tuple[str, list[str]]:
    page_name = (
        page_key.replace(
            "_",
            " ",
        ).title()
    )

    lines = []
    paths = []

    for image_path in files:
        match = VARIANT_RE.search(
            image_path.stem
        )

        variant = (
            match.group(1).title()
            if match
            else "Screen"
        )

        relative = image_path.relative_to(
            project_dir
        ).as_posix()

        paths.append(
            relative
        )

        lines.append(
            f"![{page_name}: {variant}]({relative})"
        )

    return (
        "\n\n".join(lines),
        paths,
    )


def fallback_page(
    page_key: str,
    evidence: dict,
) -> dict:
    states = evidence.get(
        "states",
        [],
    )

    main = (
        states[0].get(
            "evidence",
            {},
        )
        if states
        else {}
    )

    headings = main.get(
        "headings",
        [],
    )

    page_name = (
        headings[0]
        if headings
        else page_key.replace(
            "_",
            " ",
        ).title()
    )

    fields = []

    for field in main.get(
        "fields",
        [],
    )[:30]:
        name = (
            field.get("label")
            or field.get("placeholder")
            or field.get("name")
        )

        if name:
            fields.append(
                {
                    "name": name,
                    "description": (
                        f"Visible {field.get('type', 'field')} control"
                    ),
                    "required": bool(
                        field.get("required")
                    ),
                }
            )

    return {
        "page_key": page_key,
        "page_name": page_name,
        "summary": (
            "This page contains the controls and information shown in the captured interface."
        ),
        "route": evidence.get(
            "url",
            "",
        ),
        "roles": [],
        "tasks": [
            {
                "task_name": (
                    f"Use {page_name}"
                ),
                "action_type": "view",
                "purpose": (
                    "Review and use the visible page functions."
                ),
                "prerequisites": [],
                "steps": [
                    f"Open the {page_name} page.",
                    (
                        "Review the visible controls, fields, and table columns."
                    ),
                    (
                        "Choose the required available action for your work."
                    ),
                ],
                "fields": fields,
                "expected_result": (
                    "The requested page information or form is displayed."
                ),
                "warnings": [
                    (
                        "Only actions visible in the captured interface are documented."
                    )
                ],
                "keywords": [
                    page_name,
                    page_key.replace(
                        "_",
                        " ",
                    ),
                ],
            }
        ],
    }


def normalize_page(
    page: dict,
    page_key: str,
    evidence: dict,
) -> dict:
    result = fallback_page(
        page_key,
        evidence,
    )

    if isinstance(
        page,
        dict,
    ):
        for key in [
            "page_name",
            "summary",
            "route",
            "roles",
            "tasks",
        ]:
            if page.get(key) not in [
                None,
                "",
                [],
            ]:
                result[key] = page[key]

    result["page_key"] = (
        page_key
    )

    if (
        not isinstance(
            result.get("tasks"),
            list,
        )
        or not result["tasks"]
    ):
        result["tasks"] = fallback_page(
            page_key,
            evidence,
        )["tasks"]

    return result


def render_list(
    values: list,
    empty_text: str = (
        "None identified from the interface"
    ),
) -> str:
    if not values:
        return f"* {empty_text}"

    return "\n".join(
        f"* {value}"
        for value in values
    )


def render_fields(
    fields: list,
) -> str:
    if not fields:
        return (
            "* No specific fields were identified from the available evidence."
        )

    lines = []

    for field in fields:
        if isinstance(
            field,
            str,
        ):
            lines.append(
                f"* **{field}**"
            )

            continue

        name = (
            field.get("name")
            or "Field"
        )

        description = (
            field.get("description")
            or "Visible interface field"
        )

        required = (
            " Required."
            if field.get("required")
            else ""
        )

        lines.append(
            (
                f"* **{name}:** "
                f"{description}."
                f"{required}"
            ).replace(
                "..",
                ".",
            )
        )

    return "\n".join(
        lines
    )


def render_steps(
    steps: list,
) -> str:
    if not steps:
        return (
            "1. Open the documented page and review the visible controls."
        )

    return "\n".join(
        f"{index}. {step}"
        for index, step in enumerate(
            steps,
            start=1,
        )
    )


def render_page_markdown(
    page: dict,
    files: list[Path],
    project_dir: Path,
    module_name: str,
) -> str:
    screenshots_md, screenshot_paths = (
        image_markdown(
            page["page_key"],
            files,
            project_dir,
        )
    )

    page_name = (
        page.get("page_name")
        or page["page_key"].replace(
            "_",
            " ",
        ).title()
    )

    parts = [
        f"### Page: {page_name}",
        "",
        screenshots_md,
        "",
        (
            "**Page purpose:** "
            f"{page.get('summary') or 'Use the functions visible on this page.'}"
        ),
    ]

    if page.get("route"):
        parts.extend(
            [
                "",
                (
                    f"**Route:** "
                    f"`{page['route']}`"
                ),
            ]
        )

    for task_number, task in enumerate(
        page.get(
            "tasks",
            [],
        ),
        start=1,
    ):
        task_name = (
            task.get("task_name")
            or f"Use {page_name}"
        )

        metadata = {
            "module": module_name,
            "page": page_name,
            "task": task_name,
            "action": (
                task.get("action_type")
                or "other"
            ),
            "roles": (
                page.get("roles")
                or []
            ),
            "route": (
                page.get("route")
                or ""
            ),
            "screenshots": (
                screenshot_paths
            ),
            "keywords": (
                task.get("keywords")
                or []
            ),
            "task_order": (
                task_number
            ),
        }

        parts.extend(
            [
                "",
                (
                    "<!-- manual-meta: "
                    f"{json.dumps(metadata, ensure_ascii=False)}"
                    " -->"
                ),
                f"#### Task: {task_name}",
                "",
                (
                    "**Purpose:** "
                    f"{task.get('purpose') or page.get('summary') or 'Complete the documented task.'}"
                ),
                "",
                "**Required roles:**",
                render_list(
                    page.get("roles")
                    or [],
                    (
                        "No role restriction was identified"
                    ),
                ),
                "",
                "**Prerequisites:**",
                render_list(
                    task.get(
                        "prerequisites"
                    )
                    or []
                ),
                "",
                "**Steps:**",
                render_steps(
                    task.get("steps")
                    or []
                ),
                "",
                "**Fields and controls:**",
                render_fields(
                    task.get("fields")
                    or []
                ),
                "",
                (
                    "**Expected result:** "
                    f"{task.get('expected_result') or 'Verify the requested information or change in the software interface.'}"
                ),
                "",
                "**Warnings:**",
                render_list(
                    task.get("warnings")
                    or [],
                    (
                        "No specific warning was identified"
                    ),
                ),
                "",
                (
                    "**Search keywords:** "
                    + ", ".join(
                        task.get("keywords")
                        or [
                            task_name,
                            page_name,
                        ]
                    )
                ),
            ]
        )

    return "\n".join(
        parts
    ).strip()


def generate_module(
    client,
    model: str,
    module_name: str,
    module_dir: Path,
    software_name: str,
    purpose: str,
    audience: str,
    all_evidence: dict,
) -> str:
    files = [
        file
        for file in module_dir.iterdir()
        if file.suffix.lower()
        in IMAGE_SUFFIXES
    ]

    if not files:
        return ""

    project_dir = (
        module_dir.parent.parent
    )

    groups = group_by_page(
        files
    )

    evidence_map = module_evidence_map(
        all_evidence,
        module_name,
    )

    rendered_pages = []

    for batch in chunk_items(
        list(groups.items()),
        PAGES_PER_BATCH,
    ):
        images = []
        payload = []

        for page_key, page_files in batch:
            payload.append(
                {
                    "page_key": page_key,
                    "image_files": [
                        file.name
                        for file in page_files
                    ],
                    "ui_evidence": (
                        evidence_map.get(
                            page_key,
                            {},
                        )
                    ),
                }
            )

            images.extend(
                Image.open(file)
                for file in page_files
            )

        prompt = PROMPT.format(
            software_name=software_name,
            purpose=purpose,
            audience=audience,
            module_name=module_name,
            page_payload=json.dumps(
                payload,
                ensure_ascii=False,
                indent=2,
            ),
        )

        response = generate_content_with_retry(
            client,
            model,
            [
                *images,
                prompt,
            ],
            types.GenerateContentConfig(
                max_output_tokens=16384,
                response_mime_type=(
                    "application/json"
                ),
            ),
        )

        time.sleep(BATCH_PAUSE_SECONDS)

        try:
            parsed = parse_response_json(
                response.text
            )

            generated_pages = {
                item.get(
                    "page_key",
                    "",
                ): item
                for item in parsed.get(
                    "pages",
                    [],
                )
                if isinstance(
                    item,
                    dict,
                )
            }

        except Exception as exc:
            print(
                (
                    "  WARNING: JSON parsing failed, "
                    f"using evidence fallback: {exc}"
                )
            )

            generated_pages = {}

        for page_key, page_files in batch:
            page = normalize_page(
                generated_pages.get(
                    page_key,
                    {},
                ),
                page_key,
                evidence_map.get(
                    page_key,
                    {},
                ),
            )

            rendered_pages.append(
                render_page_markdown(
                    page,
                    page_files,
                    project_dir,
                    module_name,
                )
            )

        print(
            (
                f"  generated {len(batch)} "
                "task structured pages"
            )
        )

    return "\n\n".join(
        rendered_pages
    )


def run(
    project_dir: Path,
    software_name: str,
    purpose: str,
    audience: str,
    force: bool = False,
) -> None:
    load_dotenv()

    logger = debug_logger.get_logger(
        project_dir
    )

    model = os.getenv(
        "GEMINI_MODEL",
        DEFAULT_MODEL,
    )

    client = genai.Client()

    print(
        f"Using Gemini model: {model}"
    )

    logger.info(
        f"Section generation started using {model}"
    )

    screenshots_root = (
        project_dir
        / "screenshots"
    )

    if not screenshots_root.is_dir():
        raise RuntimeError(
            (
                "Screenshots folder not found: "
                f"{screenshots_root}"
            )
        )

    all_evidence = load_evidence(
        project_dir
    )

    module_dirs = sorted(
        directory
        for directory
        in screenshots_root.iterdir()
        if directory.is_dir()
    )

    manual_parts = [
        (
            f"# {software_name}: "
            "User Manual\n"
        ),
        (
            f"**Software purpose:** "
            f"{purpose}\n"
        ),
        (
            f"**Target audience:** "
            f"{audience}\n"
        ),
    ]

    section_number = 0

    for module_dir in module_dirs:
        module_name = (
            module_dir.name.replace(
                "_",
                " ",
            ).title()
        )

        module_slug = slug(
            module_name
        )

        module_sections_dir = (
            module_dir / "manual_sections"
        )

        module_pdf_dir = (
            module_dir / "pdf_analysis"
        )

        section_path = (
            module_sections_dir
            / f"{module_slug}.md"
        )

        if not force and section_path.is_file():
            print(
                f"Skipping module (already generated): {module_name}"
            )

            content = section_path.read_text(
                encoding="utf-8"
            )

        else:
            print(
                f"Generating module: {module_name}"
            )

            try:
                content = generate_module(
                    client,
                    model,
                    module_name,
                    module_dir,
                    software_name,
                    purpose,
                    audience,
                    all_evidence,
                )

            except Exception as exc:
                debug_logger.log_exception(
                    project_dir,
                    exc,
                    context=f"generate_module {module_name}",
                )

                raise

            if not content:
                print(
                    f"  SKIP {module_name}: no screenshots"
                )

                logger.info(
                    f"SKIP {module_name}: no screenshots"
                )

                continue

            module_sections_dir.mkdir(
                parents=True,
                exist_ok=True,
            )

            section_path.write_text(
                content,
                encoding="utf-8",
            )

            logger.info(
                f"Wrote module section: {section_path}"
            )

        module_pdf_path = (
            module_pdf_dir
            / f"{module_slug}.pdf"
        )

        if force or not module_pdf_path.is_file():
            module_html_path = (
                module_pdf_dir
                / f"{module_slug}.html"
            )

            try:
                build_pdf.render_pdf(
                    section_path,
                    module_pdf_path,
                    module_html_path,
                    project_dir,
                    subtitle=f"{module_name} module reference",
                )

                logger.info(
                    f"Wrote module PDF: {module_pdf_path}"
                )

            except Exception as exc:
                debug_logger.log_exception(
                    project_dir,
                    exc,
                    context=f"render module pdf {module_name}",
                )

        section_number += 1

        manual_parts.append(
            (
                f"## {section_number}. "
                f"{module_name} Module\n\n"
                f"{content}\n"
            )
        )

    overall_sections_dir = (
        project_dir / "manual_sections"
    )

    overall_sections_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    manual_path = (
        overall_sections_dir
        / "overall.md"
    )

    manual_path.write_text(
        "\n".join(
            manual_parts
        ),
        encoding="utf-8",
    )

    print(
        (
            "Wrote task structured manual: "
            f"{manual_path}"
        )
    )

    logger.info(
        f"Wrote overall manual: {manual_path}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__
    )

    parser.add_argument(
        "project_dir"
    )

    parser.add_argument(
        "--software-name",
        required=True,
    )

    parser.add_argument(
        "--purpose",
        required=True,
    )

    parser.add_argument(
        "--audience",
        required=True,
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate modules even if a manual_sections/*.md already exists",
    )

    args = parser.parse_args()

    run(
        Path(args.project_dir),
        args.software_name,
        args.purpose,
        args.audience,
        force=args.force,
    )


if __name__ == "__main__":
    try:
        main()

    except RuntimeError as exc:
        print(
            f"ERROR: {exc}"
        )

        raise SystemExit(1)