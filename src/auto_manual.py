"""Run the automated software manual pipeline from one command.

Available commands:
login, discover, crawl, sections, pdf, index, ask, and all.
"""

import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import crawl_engine
import discover_nav
import generate_sections
import login as login_mod

HERE = Path(__file__).parent
ROOT = HERE.parent


def project_path(project_name: str) -> Path:
    return ROOT / "projects" / project_name


def cmd_login(args) -> None:
    project_dir = project_path(args.project)
    project_dir.mkdir(parents=True, exist_ok=True)

    if not login_mod.login(
        args.login_url,
        args.username,
        args.password,
        project_dir,
    ):
        raise SystemExit(1)


def cmd_discover(args) -> None:
    project_dir = project_path(args.project)

    seed_urls = [
        url.strip()
        for url in (args.seed_urls or "").split(",")
        if url.strip()
    ]

    discover_nav.discover(
        args.base_url,
        project_dir,
        seed_urls,
    )


def cmd_crawl(args) -> None:
    crawl_engine.run(
        project_path(args.project)
    )


def cmd_sections(args) -> None:
    generate_sections.run(
        project_path(args.project),
        args.software_name,
        args.purpose,
        args.audience,
        force=args.force_regenerate,
    )


def cmd_pdf(args) -> None:
    subprocess.run(
        [
            sys.executable,
            str(HERE / "build_pdf.py"),
            str(project_path(args.project)),
        ],
        check=True,
    )


def cmd_index(args) -> None:
    command = [
        sys.executable,
        str(HERE / "index_markdown.py"),
        str(project_path(args.project)),
        "--model",
        args.embedding_model,
        "--max-chars",
        str(args.max_chars),
    ]

    if args.no_pull:
        command.append("--no-pull")

    if args.collection:
        command.extend(
            [
                "--collection",
                args.collection,
            ]
        )

    subprocess.run(
        command,
        check=True,
    )


def cmd_ask(args) -> None:
    command = [
        sys.executable,
        str(HERE / "ask_manual.py"),
        str(project_path(args.project)),
        args.question,
        "--embedding-model",
        args.embedding_model,
        "--answer-provider",
        args.answer_provider,
        "--min-confidence",
        str(args.min_confidence),
    ]

    if args.collection:
        command.extend(
            [
                "--collection",
                args.collection,
            ]
        )

    if args.no_llm_expansion:
        command.append(
            "--no-llm-expansion"
        )

    if args.answer_provider == "ollama":
        command.extend(
            [
                "--ollama-chat-model",
                args.ollama_chat_model,
            ]
        )

    subprocess.run(
        command,
        check=True,
    )


def cmd_all(args) -> None:
    project_dir = project_path(
        args.project
    )

    project_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    print("=== 1/6 Login ===")

    if not login_mod.login(
        args.login_url,
        args.username,
        args.password,
        project_dir,
    ):
        raise SystemExit(1)

    print(
        "=== 2/6 Discover navigation ==="
    )

    seed_urls = [
        url.strip()
        for url in (args.seed_urls or "").split(",")
        if url.strip()
    ]

    discover_nav.discover(
        args.base_url,
        project_dir,
        seed_urls,
    )

    print(
        "=== 3/6 Crawl screenshots and UI evidence ==="
    )

    crawl_engine.run(
        project_dir
    )

    print(
        "=== 4/6 Generate task structured manual ==="
    )

    generate_sections.run(
        project_dir,
        args.software_name,
        args.purpose,
        args.audience,
        force=args.force_regenerate,
    )

    print(
        "=== 5/6 Build PDF ==="
    )

    subprocess.run(
        [
            sys.executable,
            str(HERE / "build_pdf.py"),
            str(project_dir),
        ],
        check=True,
    )

    if args.with_index:
        print(
            "=== 6/6 Build retrieval index ==="
        )

        command = [
            sys.executable,
            str(HERE / "index_markdown.py"),
            str(project_dir),
            "--model",
            args.embedding_model,
            "--max-chars",
            str(args.max_chars),
        ]

        if args.no_pull:
            command.append(
                "--no-pull"
            )

        subprocess.run(
            command,
            check=True,
        )

    else:
        print(
            "=== 6/6 Retrieval index skipped ==="
        )

    print(
        f"Overall manual Markdown: {project_dir / 'manual_sections' / 'overall.md'}"
    )

    print(
        f"Overall manual PDF: {project_dir / 'pdf_analysis' / 'overall.pdf'}"
    )

    print(
        f"Per-menu sections and PDFs: {project_dir / 'screenshots' / '<module>' / '(manual_sections|pdf_analysis)'}"
    )

    print(
        f"Debug logs: {project_dir / 'debug'}"
    )


def add_project_argument(parser) -> None:
    parser.add_argument(
        "--project",
        required=True,
    )


def add_index_arguments(parser) -> None:
    parser.add_argument(
        "--embedding-model",
        default="qwen3-embedding:0.6b",
    )

    parser.add_argument(
        "--max-chars",
        type=int,
        default=1600,
    )

    parser.add_argument(
        "--collection"
    )

    parser.add_argument(
        "--no-pull",
        action="store_true",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    login_parser = subparsers.add_parser(
        "login"
    )

    add_project_argument(
        login_parser
    )

    login_parser.add_argument(
        "--login-url",
        required=True,
    )

    login_parser.add_argument(
        "--username",
        required=True,
    )

    login_parser.add_argument(
        "--password",
        required=True,
    )

    login_parser.set_defaults(
        func=cmd_login
    )

    discover_parser = subparsers.add_parser(
        "discover"
    )

    add_project_argument(
        discover_parser
    )

    discover_parser.add_argument(
        "--base-url",
        required=True,
    )

    discover_parser.add_argument(
        "--seed-urls",
        default="",
    )

    discover_parser.set_defaults(
        func=cmd_discover
    )

    crawl_parser = subparsers.add_parser(
        "crawl"
    )

    add_project_argument(
        crawl_parser
    )

    crawl_parser.set_defaults(
        func=cmd_crawl
    )

    sections_parser = subparsers.add_parser(
        "sections"
    )

    add_project_argument(
        sections_parser
    )

    sections_parser.add_argument(
        "--software-name",
        required=True,
    )

    sections_parser.add_argument(
        "--purpose",
        required=True,
    )

    sections_parser.add_argument(
        "--audience",
        required=True,
    )

    sections_parser.add_argument(
        "--force-regenerate",
        action="store_true",
        help="Regenerate modules even if manual_sections/*.md already exists",
    )

    sections_parser.set_defaults(
        func=cmd_sections
    )

    pdf_parser = subparsers.add_parser(
        "pdf"
    )

    add_project_argument(
        pdf_parser
    )

    pdf_parser.set_defaults(
        func=cmd_pdf
    )

    index_parser = subparsers.add_parser(
        "index"
    )

    add_project_argument(
        index_parser
    )

    add_index_arguments(
        index_parser
    )

    index_parser.set_defaults(
        func=cmd_index
    )

    ask_parser = subparsers.add_parser(
        "ask"
    )

    add_project_argument(
        ask_parser
    )

    ask_parser.add_argument(
        "question"
    )

    ask_parser.add_argument(
        "--embedding-model",
        default="qwen3-embedding:0.6b",
    )

    ask_parser.add_argument(
        "--collection"
    )

    ask_parser.add_argument(
        "--answer-provider",
        choices=[
            "gemini",
            "ollama",
            "none",
        ],
        default="gemini",
    )

    ask_parser.add_argument(
        "--ollama-chat-model",
        default="qwen3:4b",
    )

    ask_parser.add_argument(
        "--min-confidence",
        type=float,
        default=0.34,
    )

    ask_parser.add_argument(
        "--no-llm-expansion",
        action="store_true",
    )

    ask_parser.set_defaults(
        func=cmd_ask
    )

    all_parser = subparsers.add_parser(
        "all"
    )

    add_project_argument(
        all_parser
    )

    all_parser.add_argument(
        "--login-url",
        required=True,
    )

    all_parser.add_argument(
        "--username",
        required=True,
    )

    all_parser.add_argument(
        "--password",
        required=True,
    )

    all_parser.add_argument(
        "--base-url",
        required=True,
    )

    all_parser.add_argument(
        "--seed-urls",
        default="",
    )

    all_parser.add_argument(
        "--software-name",
        required=True,
    )

    all_parser.add_argument(
        "--purpose",
        required=True,
    )

    all_parser.add_argument(
        "--audience",
        required=True,
    )

    all_parser.add_argument(
        "--with-index",
        action="store_true",
    )

    all_parser.add_argument(
        "--force-regenerate",
        action="store_true",
        help="Regenerate manual sections even if manual_sections/*.md already exists",
    )

    add_index_arguments(
        all_parser
    )

    all_parser.set_defaults(
        func=cmd_all
    )

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()