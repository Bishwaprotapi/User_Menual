# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Project Overview

This is a **batch content-generation tool** that turns a piece of software's
UI into a polished Markdown + PDF user manual, either from a handful of
manually-dropped screenshots or from a full Playwright crawl of every page
in an app.

- **Language:** Python 3
- **LLM stack:** Google Gemini (`google-genai`) for the lightweight generic
  flow; Codex (via chat, using `agent_prompts/*.txt`) for full crawler-based
  projects
- **Rendering:** `markdown-it-py` (Markdown → HTML) + Playwright/headless
  Chromium (HTML → PDF)
- **No web server, no database** — this is a CLI/script tool, not an API.

## Running & Development

```bash
pip install -r requirements.txt
playwright install chromium   # one-time, needed for crawling and PDF export
```

**Generic flow** (a few screenshots, one software):
```bash
py src/generate_manual.py --name "TaskFlow Pro" --purpose "Project Management" --audience "Non-technical managers"
```
Reads `screenshots/`, fills `config/PROMPT_TEMPLATE.md`, calls Gemini, writes `manual.md`.

**Full crawler flow** (every page of a real app, e.g. `projects/peopledesk/`):
1. `projects/<name>/crawl.py` logs in with a saved Playwright `auth_state.json`
   and screenshots every page (list view + best-effort Create/Edit/Show modals)
   listed in that project's `discovery.json`.
2. Screenshots are grouped by module and fed through `agent_prompts/*.txt`
   (one prompt per module) in a Codex chat to produce `manual_sections/*.md`.
3. Sections are concatenated into `manual.md`.
4. `py src/build_pdf.py projects/<name>` renders `manual.md` to a styled
   `manual.pdf` (cover page, table of contents, page numbers).

**There is no test framework.** This is a small, mostly-manual pipeline —
verification is "does the generated manual/PDF look right," not unit tests.

## Architecture

```
config/PROMPT_TEMPLATE.md   # generic LLM prompt, used by the generic flow
src/generate_manual.py       # generic flow: screenshots/ -> Gemini -> manual.md
src/build_pdf.py             # any projects/<name>/manual.md -> styled manual.pdf
screenshots/                 # dropzone for the generic flow (input images)
projects/<name>/             # one folder per fully-crawled software
  crawl.py                     # site-specific Playwright crawler + page list
  auth_state.json              # saved login session (Playwright storage_state)
  discovery.json               # module -> nav links, as discovered from the live app
  page_map.json                # module -> screenshot files, for completeness checks
  screenshots/<module>/         # crawled page + create/edit/show screenshots
  agent_prompts/<module>.txt    # per-module manual-writing prompt for Codex
  manual_sections/<module>.md   # per-module generated manual content
  manual.md / manual.html / manual.pdf   # assembled manual, in 3 formats
```

Adding a new full-crawler project means: create `projects/<name>/`, write a
`discovery.json` (module → nav links) and `crawl.py` against it (copy
`projects/peopledesk/crawl.py` as a starting point — it's already generic
over "any module list + auth_state.json"), run it to populate
`screenshots/`, write one `agent_prompts/*.txt` per module, generate
`manual_sections/*.md` via chat, concatenate into `manual.md`, then run
`src/build_pdf.py projects/<name>`.

## Key Files

| File | Purpose |
|---|---|
| `src/generate_manual.py` | Generic screenshots → Gemini → `manual.md` flow |
| `src/build_pdf.py` | Renders any project's `manual.md` to a styled PDF |
| `config/PROMPT_TEMPLATE.md` | LLM prompt template for the generic flow |
| `projects/peopledesk/crawl.py` | Reference crawler implementation (Playwright, best-effort Create/Edit/Show capture) |
| `projects/peopledesk/discovery.json` | Module → nav-link map, scraped from the live app's sidebar |
| `projects/peopledesk/page_map.json` | Module → expected screenshot files, used to verify nothing's missing |

## Important Patterns

- **Screenshot completeness check:** compare `page_map.json`'s file list
  against what's actually on disk (and check for broken `![...]()` image
  refs in `manual.md`) before considering a project's manual done.
- **Nav-drift check:** re-visit each module's base URL from `discovery.json`
  and diff the live sidebar `<a href>`s against the recorded `links` list to
  catch new/removed pages before re-crawling everything.
- **PDF regeneration:** re-run `src/build_pdf.py projects/<name>` any time
  `manual.md` changes — it's a full rebuild (cover + TOC + all pages), not
  incremental.
