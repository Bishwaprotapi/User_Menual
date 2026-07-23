"""Render any manual.md (+ its screenshots) to a styled PDF via headless Chrome.

Exposes render_pdf() so both the per-module PDFs (screenshots/<module>/pdf_analysis/)
and the project-wide Overall PDF (pdf_analysis/overall.pdf) share one renderer.
"""
import argparse
import re
from pathlib import Path
from markdown_it import MarkdownIt
from playwright.sync_api import sync_playwright

CSS = """
body { font-family: -apple-system, Segoe UI, Arial, sans-serif; color: #1f2430; line-height: 1.5; }
.cover { height: 90vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; page-break-after: always; }
.cover h1 { font-size: 40px; margin-bottom: 8px; }
.cover p { color: #667; }
nav.toc { page-break-after: always; }
nav.toc h2 { font-size: 22px; }
nav.toc ul { list-style: none; padding-left: 0; }
nav.toc li { margin: 6px 0; }
nav.toc a { color: #1a4fd6; text-decoration: none; }
h2 { font-size: 24px; border-bottom: 2px solid #ddd; padding-bottom: 6px; margin-top: 40px; page-break-before: always; }
h3 { font-size: 19px; color: #17305a; margin-top: 30px; }
h4 { font-size: 17px; color: #17305a; margin-top: 28px; }
img { max-width: 100%; border: 1px solid #ddd; border-radius: 4px; margin: 10px 0; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; }
th, td { border: 1px solid #ccc; padding: 6px 10px; text-align: left; font-size: 13px; }
code { background: #f2f2f2; padding: 1px 4px; border-radius: 3px; }
"""


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.strip().lower()).strip("-")


def render_pdf(
    md_path: Path,
    pdf_path: Path,
    html_path: Path,
    base_dir: Path,
    subtitle: str = "Generated user manual with step-by-step screenshots",
) -> None:
    """Render one manual.md to manual.pdf.

    Image src paths inside md_path are resolved relative to base_dir (not
    md_path's own folder), via a <base href> tag, so a per-module manual
    living under screenshots/<module>/manual_sections/ can still reference
    screenshots one level up with a plain relative path.
    """
    md_text = md_path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+)$", md_text, re.M)
    title = title_match.group(1) if title_match else "User Manual"

    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    body_html = md.render(md_text)

    toc_entries = []

    def add_anchor(m):
        text = m.group(1)
        anchor = slugify(text)
        toc_entries.append((anchor, text))
        return f'<h2 id="{anchor}">{text}</h2>'

    body_html = re.sub(r"<h2>(.+?)</h2>", add_anchor, body_html)

    toc_html = "\n".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in toc_entries)

    base_uri = base_dir.resolve().as_uri() + "/"

    html = f"""<!doctype html><html><head><meta charset="utf-8">
<base href="{base_uri}">
<title>{title}</title><style>{CSS}</style></head><body>
<div class="cover"><h1>{title}</h1><p>{subtitle}</p></div>
<nav class="toc"><h2>Table of Contents</h2><ul>{toc_html}</ul></nav>
{body_html}
</body></html>"""

    html_path.parent.mkdir(parents=True, exist_ok=True)
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html, encoding="utf-8")

    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        pg = b.new_page()
        pg.goto(html_path.resolve().as_uri())
        pg.wait_for_timeout(500)
        pg.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "20mm", "bottom": "18mm", "left": "15mm", "right": "15mm"},
            display_header_footer=True,
            header_template="<div></div>",
            footer_template='<div style="font-size:9px;width:100%;text-align:center;color:#888;">'
            '<span class="pageNumber"></span> / <span class="totalPages"></span></div>',
        )
        b.close()

    print(f"Wrote {pdf_path} ({pdf_path.stat().st_size // 1024} KB)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", help="Path to the project folder, e.g. projects/peopledesk")
    args = parser.parse_args()

    project_dir = Path(args.project_dir)

    md_path = project_dir / "manual_sections" / "overall.md"
    if not md_path.is_file():
        md_path = project_dir / "manual.md"  # older projects, generated before this layout

    pdf_path = project_dir / "pdf_analysis" / "overall.pdf"
    html_path = project_dir / "pdf_analysis" / "overall.html"

    render_pdf(md_path, pdf_path, html_path, project_dir)


if __name__ == "__main__":
    main()
