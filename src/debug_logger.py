"""Structured debug logging shared by every pipeline stage.

Writes to <project_dir>/debug/: execution.log (all steps), warnings.log,
errors.log, console.log (browser console messages), and exceptions.log
(full Python + browser page-error tracebacks). This is what a future
troubleshooting pass reads instead of scrollback.
"""

import logging
import traceback
from pathlib import Path

_LOGGERS: dict[str, logging.Logger] = {}


def get_logger(project_dir: Path) -> logging.Logger:
    project_dir = Path(project_dir)
    key = str(project_dir.resolve())

    if key in _LOGGERS:
        return _LOGGERS[key]

    debug_dir = project_dir / "debug"
    debug_dir.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(f"manual.{key}")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    for filename, level in (
        ("execution.log", logging.INFO),
        ("warnings.log", logging.WARNING),
        ("errors.log", logging.ERROR),
    ):
        handler = logging.FileHandler(debug_dir / filename, encoding="utf-8")
        handler.setLevel(level)
        handler.setFormatter(fmt)
        logger.addHandler(handler)

    _LOGGERS[key] = logger
    return logger


def log_exception(project_dir: Path, exc: BaseException, context: str = "") -> None:
    """Record a Python exception's full traceback to debug/exceptions.log."""
    project_dir = Path(project_dir)
    debug_dir = project_dir / "debug"
    debug_dir.mkdir(parents=True, exist_ok=True)

    trace_text = "".join(
        traceback.format_exception(type(exc), exc, exc.__traceback__)
    )

    with (debug_dir / "exceptions.log").open("a", encoding="utf-8") as fh:
        fh.write(f"\n--- {context or exc.__class__.__name__} ---\n{trace_text}\n")

    get_logger(project_dir).error(f"{context}: {exc}" if context else str(exc))


def attach_browser_logging(page, project_dir: Path) -> None:
    """Pipe a Playwright page's console output and JS errors to debug/*.log."""
    project_dir = Path(project_dir)
    debug_dir = project_dir / "debug"
    debug_dir.mkdir(parents=True, exist_ok=True)

    console_path = debug_dir / "console.log"
    exceptions_path = debug_dir / "exceptions.log"

    def on_console(msg) -> None:
        try:
            with console_path.open("a", encoding="utf-8") as fh:
                fh.write(f"[{msg.type}] {page.url} :: {msg.text}\n")
        except Exception:
            pass

    def on_pageerror(exc) -> None:
        try:
            with exceptions_path.open("a", encoding="utf-8") as fh:
                fh.write(f"[browser pageerror] {page.url} :: {exc}\n")
        except Exception:
            pass

    page.on("console", on_console)
    page.on("pageerror", on_pageerror)
