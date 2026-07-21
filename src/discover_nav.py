"""Discover an app's page list by BFS-crawling same-origin <a href> links.

Finds every page reachable through a real link from the base URL (or the
optional --seed-urls, for sections hidden behind a JS click-to-expand menu
with no plain href on the top-level item — same gap PeopleDesk's own
hamburger drawer would have hit). Groups pages by their first URL path
segment and writes discovery.json in the shape crawl_engine.py expects.
"""
import argparse
import json
import re
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlparse

from playwright.sync_api import sync_playwright

SKIP_RE = re.compile(r"logout|log-out|sign-?out|delete|remove|export|mailto:|tel:|javascript:", re.I)
MAX_DEPTH = 2
MAX_PAGES = 300


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.strip().lower()).strip("_") or "root"


def same_origin(url: str, origin: str) -> bool:
    return urlparse(url).netloc == urlparse(origin).netloc


def discover(base_url: str, project_dir: Path, seed_urls=None) -> dict:
    origin = f"{urlparse(base_url).scheme}://{urlparse(base_url).netloc}"
    seen_pages = {}  # href_path -> text
    queue = deque([(base_url, 0)])
    for u in seed_urls or []:
        queue.append((u, 0))
    visited_pages = set()

    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        ctx = b.new_context(storage_state=str(project_dir / "auth_state.json"), viewport={"width": 1920, "height": 1000})
        pg = ctx.new_page()

        while queue and len(visited_pages) < MAX_PAGES:
            url, depth = queue.popleft()
            path = urlparse(url).path
            if path in visited_pages:
                continue
            visited_pages.add(path)

            try:
                pg.goto(url, timeout=20000)
            except Exception as e:
                print(f"FAIL loading {url}: {e}")
                continue
            try:
                pg.wait_for_load_state("networkidle", timeout=8000)
            except Exception:
                pass
            pg.wait_for_timeout(800)

            links = pg.eval_on_selector_all(
                "a[href]",
                "els => els.map(e => ({href: e.getAttribute('href'), text: e.innerText.trim()}))",
            )
            for link in links:
                href = link.get("href") or ""
                text = link.get("text") or ""
                if not href or SKIP_RE.search(href) or SKIP_RE.search(text):
                    continue
                abs_url = urljoin(url, href)
                if not same_origin(abs_url, origin):
                    continue
                link_path = urlparse(abs_url).path
                if not link_path or link_path == "/":
                    continue
                if link_path not in seen_pages:
                    seen_pages[link_path] = text or link_path
                if link_path not in visited_pages and depth + 1 <= MAX_DEPTH:
                    queue.append((abs_url, depth + 1))

        ctx.close()
        b.close()

    modules = {}
    for path, text in sorted(seen_pages.items()):
        segment = path.strip("/").split("/")[0] if path.strip("/") else "root"
        module_name = segment.replace("-", " ").replace("_", " ").title()
        modules.setdefault(module_name, {"url": origin + path, "links": []})
        modules[module_name]["links"].append({"text": text, "href": path})

    discovery = {"base_url": origin, **modules}
    (project_dir / "discovery.json").write_text(json.dumps(discovery, indent=2), encoding="utf-8")
    print(f"Discovered {len(seen_pages)} pages across {len(modules)} modules -> {project_dir / 'discovery.json'}")
    return discovery


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", help="Path to the project folder, e.g. projects/newsoftware")
    parser.add_argument("base_url", help="Landing page URL to start the BFS from")
    parser.add_argument("--seed-urls", default="", help="Comma-separated extra starting URLs for sections hidden behind click-to-expand menus")
    args = parser.parse_args()

    project_dir = Path(args.project_dir)
    seed_urls = [u.strip() for u in args.seed_urls.split(",") if u.strip()]
    discover(args.base_url, project_dir, seed_urls)


if __name__ == "__main__":
    main()
