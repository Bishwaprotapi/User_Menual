# User Manual Generator

Turns software screenshots into a polished Markdown (+ PDF) user manual.

## Manual usage (chat)
1. Drop screenshot(s) into `screenshots/`.
2. Open `config/PROMPT_TEMPLATE.md` and fill in the three brackets: Software Name, Core Purpose, Target Audience.
3. Give Claude the filled-in prompt plus the screenshot(s); it writes the manual.

## Automated usage (script)
1. `pip install -r requirements.txt` (also run `playwright install chromium` once, for PDF export)
2. Get a free API key at https://aistudio.google.com/apikey and set `GEMINI_API_KEY` in your environment.
3. Drop screenshot(s) into `screenshots/`.
4. Run:
   ```
   py src/generate_manual.py --name "TaskFlow Pro" --purpose "Project Management" --audience "Non-technical managers"
   ```
5. Output is written to `manual.md` (override with `--output`).

## Full crawler-based projects

For a whole application (every page, screenshotted and documented), each
software gets its own folder under `projects/<name>/` — see
`projects/peopledesk/` for a complete example. That folder owns its
`crawl.py` (Playwright script + page list), `auth_state.json` (login
session), the crawled `screenshots/`, per-module `agent_prompts/` /
`manual_sections/`, and the assembled `manual.md`.

To export a project's manual to PDF (cover page, table of contents, page
numbers):
```
py src/build_pdf.py projects/peopledesk
```

## New software, one command

Given a login URL, username, and password, this does the whole pipeline —
login, discover pages, crawl screenshots, write the manual via Gemini, build
the PDF:
```
py src/auto_manual.py all --project <name> ^
  --login-url <url> --username <user> --password <pass> ^
  --base-url <url> ^
  --software-name "<name>" --purpose "<purpose>" --audience "<audience>"
```
Requires `GEMINI_API_KEY` in a `.env` file at the repo root (or the real
environment). Each step also runs on its own — `login`, `discover`, `crawl`,
`sections`, `pdf` — see `py src/auto_manual.py -h`.

Two honest limits:
- **Login** is a generic heuristic (single-page or Google/Microsoft-style
  two-step form). It can't solve CAPTCHAs or MFA. If it fails, check the
  screenshots it saves to `projects/<name>/debug/`.
- **Discovery** only finds pages reachable through a real `<a href>` link.
  Sections hidden behind a JS click-to-expand menu with no plain href on the
  top-level item won't be found automatically — pass one known URL per such
  section via `--seed-urls url1,url2`.

## PDF analysis: PixelRAG vs Docling

Install the dependencies, then compare the visual PixelRAG representation,
plain extracted text, and Docling's structured output for a generated manual:

```powershell
pip install -r requirements.txt
py src/analyze_pdf.py projects/iprimevatmanual
```

On Windows, bundled Codex Poppler is detected automatically. Otherwise pass
`--poppler-path "C:\path\to\poppler\Library\bin"`.

Results are written to `projects/iprimevatmanual/pdf_analysis/`:

- `pixelrag/tiles/` and `pixelrag/manifest.json`: visual PixelRAG output
- `raw_text.txt`: flat text-extraction baseline
- `docling/structured.md` and `docling/structured.json`: Docling output
- `README.md`: generated comparison report with metrics and output links

PixelRAG is pixel-native and does not extract text. Docling processes the
original PDF directly so it can reconstruct headings, tables, lists, layout,
and reading order.

## Embed the structured manual with Ollama and ChromaDB

After PDF analysis has produced `pdf_analysis/docling/structured.md`, pull the
Qwen3 embedding model, create heading-aware chunks with LangChain's
`MarkdownHeaderTextSplitter`, and persist them in Chroma:

```powershell
py src/index_markdown.py projects/iprimevatmanual
```

The command uses Ollama model `qwen3-embedding:0.6b`, stores vectors under
`pdf_analysis/chroma_db/`, and writes `EMBEDDING_README.md` plus the complete
machine-readable `embedding_report.json`. Use `--query "your question"` to
change the semantic-search verification query.
