"""Compare PixelRAG visual rendering, raw PDF text, and Docling structure."""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

from PIL import Image


def find_poppler_bin(explicit_path: str | None = None) -> Path | None:
    candidates = []
    if explicit_path:
        candidates.append(Path(explicit_path).expanduser())
    env_path = os.getenv("POPPLER_PATH")
    if env_path:
        candidates.append(Path(env_path).expanduser())
    candidates.append(
        Path.home()
        / ".cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin"
    )
    for candidate in candidates:
        if (candidate / "pdfinfo.exe").is_file() and (candidate / "pdftoppm.exe").is_file():
            return candidate.resolve()
    if shutil.which("pdfinfo") and shutil.which("pdftoppm"):
        return None
    return None


def run_pixelrag(
    pdf_path: Path, output_dir: Path, dpi: int, poppler_path: str | None = None
) -> dict:
    pixelshot = shutil.which("pixelshot")
    if not pixelshot:
        raise RuntimeError("pixelshot is missing; install with: pip install 'pixelrag[pdf]'")
    tiles_dir = output_dir / "tiles"
    tiles_dir.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    env = os.environ.copy()
    poppler_bin = find_poppler_bin(poppler_path)
    if poppler_bin:
        env["PATH"] = f"{poppler_bin}{os.pathsep}{env.get('PATH', '')}"
        print(f"Using Poppler: {poppler_bin}")
    elif not (shutil.which("pdfinfo") and shutil.which("pdftoppm")):
        raise RuntimeError(
            "Poppler was not found. Install it or pass --poppler-path pointing "
            "to the folder containing pdfinfo.exe and pdftoppm.exe."
        )
    subprocess.run(
        [pixelshot, str(pdf_path), "--output", str(tiles_dir), "--dpi", str(dpi)],
        check=True,
        env=env,
    )
    tiles = []
    for path in sorted(tiles_dir.rglob("*")):
        if path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
            continue
        with Image.open(path) as image:
            width, height = image.size
        tiles.append({
            "file": path.relative_to(output_dir).as_posix(),
            "width": width,
            "height": height,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        })
    result = {
        "engine": "PixelRAG pixelshot",
        "source": str(pdf_path.resolve()),
        "dpi": dpi,
        "elapsed_seconds": round(time.perf_counter() - started, 3),
        "tile_count": len(tiles),
        "note": "PixelRAG produces visual tiles, not extracted text.",
        "tiles": tiles,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "manifest.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def extract_raw_text(pdf_path: Path, output_path: Path) -> dict:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError("pypdf is missing; install with: pip install pypdf") from exc
    started = time.perf_counter()
    reader = PdfReader(str(pdf_path))
    pages = [
        f"===== PAGE {number} =====\n\n{page.extract_text() or ''}"
        for number, page in enumerate(reader.pages, start=1)
    ]
    content = "\n\n".join(pages)
    output_path.write_text(content, encoding="utf-8")
    return {
        "page_count": len(reader.pages),
        "characters": len(content),
        "elapsed_seconds": round(time.perf_counter() - started, 3),
    }


def run_docling(pdf_path: Path, output_dir: Path) -> dict:
    try:
        from docling.document_converter import DocumentConverter
    except ImportError as exc:
        raise RuntimeError("docling is missing; install with: pip install docling") from exc
    output_dir.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    document = DocumentConverter().convert(str(pdf_path)).document
    markdown = document.export_to_markdown()
    structured = document.export_to_dict()
    (output_dir / "structured.md").write_text(markdown, encoding="utf-8")
    (output_dir / "structured.json").write_text(
        json.dumps(structured, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return {
        "markdown_characters": len(markdown),
        "elapsed_seconds": round(time.perf_counter() - started, 3),
    }


def write_report(output_dir: Path, pdf_path: Path, pixelrag: dict, raw: dict, docling: dict) -> None:
    examples = "\n".join(
        f"- [{item['file']}]({item['file']}) ({item['width']}x{item['height']})"
        for item in pixelrag["tiles"][:10]
    ) or "- No tiles were produced."
    report = f"""# PDF Analysis: {pdf_path.name}

This report compares three representations of the same PDF. PixelRAG preserves
pages visually, pypdf provides a flat-text baseline, and Docling reconstructs
layout-aware Markdown and structured JSON.

## Summary

| Stage | Output | Result | Time |
|---|---|---:|---:|
| PixelRAG | Visual tiles | {pixelrag['tile_count']} tiles | {pixelrag['elapsed_seconds']}s |
| pypdf | Flat text | {raw['characters']} characters / {raw['page_count']} pages | {raw['elapsed_seconds']}s |
| Docling | Markdown + JSON | {docling['markdown_characters']} Markdown characters | {docling['elapsed_seconds']}s |

## PixelRAG output

PixelRAG does not extract text. It renders visual tiles for pixel-native
retrieval, retaining screenshots, tables, charts, and layout. See the complete
[manifest](pixelrag/manifest.json).

{examples}

## Raw text baseline

[Open raw_text.txt](raw_text.txt) to inspect traditional text extraction and
reading-order or table-flattening issues.

## Docling structured output

- [Open structured Markdown](docling/structured.md)
- [Open structured JSON](docling/structured.json)

Docling processes the original PDF directly. Passing already-flattened text to
it would discard the geometry needed to recover headings, tables, lists, and
reading order.

## Interpretation

- Use PixelRAG when retrieval must understand how a page looks.
- Use Docling when downstream processing needs semantic document structure.
- Use raw text as a diagnostic baseline, not as Docling's input.
"""
    (output_dir / "README.md").write_text(report, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", help="Project folder containing manual.pdf")
    parser.add_argument("--pdf", help="PDF path; defaults to <project>/manual.pdf")
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument(
        "--poppler-path",
        help="Folder containing pdfinfo/pdftoppm; bundled Codex Poppler is auto-detected",
    )
    args = parser.parse_args()

    project_dir = Path(args.project_dir).resolve()
    pdf_path = Path(args.pdf).resolve() if args.pdf else project_dir / "manual.pdf"
    if not pdf_path.is_file():
        raise SystemExit(f"PDF not found: {pdf_path}")
    output_dir = project_dir / "pdf_analysis"
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=== 1/3 PixelRAG visual rendering ===")
    pixelrag = run_pixelrag(
        pdf_path, output_dir / "pixelrag", args.dpi, args.poppler_path
    )
    print(f"PixelRAG produced {pixelrag['tile_count']} tiles")
    print("=== 2/3 raw text baseline ===")
    raw = extract_raw_text(pdf_path, output_dir / "raw_text.txt")
    print(f"Raw extraction produced {raw['characters']} characters")
    print("=== 3/3 Docling structured conversion ===")
    docling = run_docling(pdf_path, output_dir / "docling")
    print(f"Docling produced {docling['markdown_characters']} Markdown characters")
    write_report(output_dir, pdf_path, pixelrag, raw, docling)
    print(f"Done: {output_dir / 'README.md'}")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
