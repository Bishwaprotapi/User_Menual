"""Create a clean, task aware ChromaDB index from a generated manual."""

import argparse
import hashlib
import json
import math
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

META_TASK_RE = re.compile(
    r"<!--\s*manual-meta:\s*(\{.*?\})\s*-->\s*\n"
    r"####\s+Task:\s*(.+?)\s*\n"
    r"(.*?)(?=\n<!--\s*manual-meta:|\Z)",
    re.DOTALL,
)


def sha256_text(
    text: str,
) -> str:
    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


def safe_collection_name(
    value: str,
) -> str:
    cleaned = re.sub(
        r"[^a-zA-Z0-9._-]+",
        "_",
        value,
    ).strip("._-")

    if len(cleaned) < 3:
        cleaned = (
            f"manual_{cleaned or 'index'}"
        )

    return cleaned[:200]


def parse_task_sections(
    markdown: str,
    max_chars: int,
) -> list[dict]:
    try:
        from langchain_text_splitters import (
            RecursiveCharacterTextSplitter,
        )

    except ImportError as exc:
        raise RuntimeError(
            (
                "langchain-text-splitters is missing. "
                "Install it using "
                "pip install langchain-text-splitters"
            )
        ) from exc

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=max_chars,
        chunk_overlap=min(
            220,
            max_chars // 8,
        ),
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
    )

    sections = []

    for section_index, match in enumerate(
        META_TASK_RE.finditer(
            markdown
        )
    ):
        metadata_text, task_heading, body = (
            match.groups()
        )

        try:
            metadata = json.loads(
                metadata_text
            )

        except json.JSONDecodeError:
            metadata = {}

        metadata["task"] = (
            metadata.get("task")
            or task_heading.strip()
        )

        module = metadata.get(
            "module",
            "Unknown module",
        )

        page = metadata.get(
            "page",
            "Unknown page",
        )

        task = metadata.get(
            "task",
            task_heading.strip(),
        )

        keywords = (
            metadata.get("keywords")
            or []
        )

        roles = (
            metadata.get("roles")
            or []
        )

        enriched = (
            f"Module: {module}\n"
            f"Page: {page}\n"
            f"Task: {task}\n"
            f"Action: {metadata.get('action', 'other')}\n"
            f"Roles: {', '.join(roles)}\n"
            f"Keywords: {', '.join(keywords)}\n\n"
            f"{body.strip()}"
        )

        pieces = splitter.split_text(
            enriched
        )

        task_id = sha256_text(
            (
                f"{module}|"
                f"{page}|"
                f"{task}|"
                f"{section_index}"
            )
        )

        for part_index, piece in enumerate(
            pieces
        ):
            sections.append(
                {
                    "heading": (
                        f"{module} > "
                        f"{page} > "
                        f"{task}"
                    ),
                    "text": piece.strip(),
                    "metadata": metadata,
                    "task_id": task_id,
                    "section_index": (
                        section_index
                    ),
                    "part_index": (
                        part_index
                    ),
                    "part_count": (
                        len(pieces)
                    ),
                }
            )

    return sections


def fallback_split(
    markdown: str,
    max_chars: int,
) -> list[dict]:
    try:
        from langchain_text_splitters import (
            MarkdownHeaderTextSplitter,
            RecursiveCharacterTextSplitter,
        )

    except ImportError as exc:
        raise RuntimeError(
            (
                "langchain-text-splitters is missing. "
                "Install it using "
                "pip install langchain-text-splitters"
            )
        ) from exc

    headers = [
        (
            "#" * level,
            f"Header {level}",
        )
        for level in range(
            1,
            7,
        )
    ]

    header_splitter = (
        MarkdownHeaderTextSplitter(
            headers_to_split_on=headers,
            strip_headers=False,
        )
    )

    documents = (
        header_splitter.split_text(
            markdown
        )
    )

    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=max_chars,
            chunk_overlap=min(
                220,
                max_chars // 8,
            ),
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )
    )

    pieces = splitter.split_documents(
        documents
    )

    chunks = []

    for index, document in enumerate(
        pieces
    ):
        headings = [
            document.metadata.get(
                f"Header {level}"
            )
            for level in range(
                1,
                7,
            )
            if document.metadata.get(
                f"Header {level}"
            )
        ]

        text = (
            document.page_content.strip()
        )

        if not text:
            continue

        heading = (
            " > ".join(headings)
            or "Document"
        )

        chunks.append(
            {
                "heading": heading,
                "text": (
                    f"Heading: {heading}\n\n"
                    f"{text}"
                ),
                "metadata": {
                    "module": (
                        headings[1]
                        if len(headings) > 1
                        else ""
                    ),
                    "page": (
                        headings[2]
                        if len(headings) > 2
                        else ""
                    ),
                    "task": (
                        headings[-1]
                        if headings
                        else "Document"
                    ),
                    "action": "other",
                    "roles": [],
                    "route": "",
                    "screenshots": [],
                    "keywords": headings,
                },
                "task_id": sha256_text(
                    (
                        f"fallback|"
                        f"{heading}|"
                        f"{index}"
                    )
                ),
                "section_index": index,
                "part_index": 0,
                "part_count": 1,
            }
        )

    return chunks


def split_manual(
    markdown: str,
    max_chars: int,
) -> list[dict]:
    if max_chars < 500:
        raise RuntimeError(
            "max chars must be at least 500"
        )

    task_chunks = parse_task_sections(
        markdown,
        max_chars,
    )

    return (
        task_chunks
        or fallback_split(
            markdown,
            max_chars,
        )
    )


def ollama_embed(
    base_url: str,
    model: str,
    texts: list[str],
) -> list[list[float]]:
    payload = json.dumps(
        {
            "model": model,
            "input": texts,
            "truncate": True,
        }
    ).encode("utf-8")

    request = urllib.request.Request(
        (
            f"{base_url.rstrip('/')}"
            "/api/embed"
        ),
        data=payload,
        headers={
            "Content-Type": (
                "application/json"
            )
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(
            request,
            timeout=600,
        ) as response:
            result = json.loads(
                response.read().decode(
                    "utf-8"
                )
            )

    except urllib.error.URLError as exc:
        detail = (
            exc.read().decode(
                "utf-8",
                errors="replace",
            )
            if hasattr(exc, "read")
            else str(exc)
        )

        raise RuntimeError(
            (
                "Ollama embedding request failed: "
                f"{detail}"
            )
        ) from exc

    embeddings = result.get(
        "embeddings",
        [],
    )

    if len(embeddings) != len(texts):
        raise RuntimeError(
            (
                f"Ollama returned {len(embeddings)} "
                f"vectors for {len(texts)} texts"
            )
        )

    return embeddings


def pull_model(
    model: str,
) -> None:
    executable = shutil.which(
        "ollama"
    )

    if not executable:
        raise RuntimeError(
            "Ollama command was not found"
        )

    subprocess.run(
        [
            executable,
            "pull",
            model,
        ],
        check=True,
    )


def validate_embeddings(
    embeddings: list[list[float]],
) -> tuple[int, float]:
    if not embeddings:
        raise RuntimeError(
            "No embeddings were generated"
        )

    dimension = len(
        embeddings[0]
    )

    if dimension == 0:
        raise RuntimeError(
            "Embedding dimension is zero"
        )

    for index, vector in enumerate(
        embeddings
    ):
        if len(vector) != dimension:
            raise RuntimeError(
                (
                    "Embedding dimension mismatch "
                    f"at vector {index}"
                )
            )

        if not all(
            math.isfinite(value)
            for value in vector
        ):
            raise RuntimeError(
                (
                    f"Embedding vector {index} "
                    "contains invalid values"
                )
            )

    norm = math.sqrt(
        sum(
            value * value
            for value in embeddings[0]
        )
    )

    if (
        norm <= 0
        or not math.isfinite(norm)
    ):
        raise RuntimeError(
            "The first vector norm is invalid"
        )

    return dimension, norm


def scalar_metadata(
    chunk: dict,
    source_info: dict,
    indexed_at: str,
) -> dict:
    metadata = chunk[
        "metadata"
    ]

    return {
        "heading": chunk["heading"],
        "module": str(
            metadata.get("module")
            or ""
        ),
        "page": str(
            metadata.get("page")
            or ""
        ),
        "task": str(
            metadata.get("task")
            or ""
        ),
        "action": str(
            metadata.get("action")
            or "other"
        ),
        "route": str(
            metadata.get("route")
            or ""
        ),
        "roles_json": json.dumps(
            metadata.get("roles")
            or [],
            ensure_ascii=False,
        ),
        "screenshots_json": json.dumps(
            metadata.get("screenshots")
            or [],
            ensure_ascii=False,
        ),
        "keywords_json": json.dumps(
            metadata.get("keywords")
            or [],
            ensure_ascii=False,
        ),
        "task_id": (
            chunk["task_id"]
        ),
        "section_index": int(
            chunk["section_index"]
        ),
        "part_index": int(
            chunk["part_index"]
        ),
        "part_count": int(
            chunk["part_count"]
        ),
        "project": (
            source_info["project"]
        ),
        "source": (
            source_info["source"]
        ),
        "source_id": (
            source_info["source_id"]
        ),
        "source_sha256": (
            source_info["source_sha256"]
        ),
        "embedding_model": (
            source_info["model"]
        ),
        "indexed_at": indexed_at,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__
    )

    parser.add_argument(
        "project_dir"
    )

    parser.add_argument(
        "--markdown",
        help=(
            "Defaults to project manual_sections/overall.md "
            "(falls back to manual.md for older projects)"
        ),
    )

    parser.add_argument(
        "--model",
        default="qwen3-embedding:0.6b",
    )

    parser.add_argument(
        "--ollama-url",
        default="http://localhost:11434",
    )

    parser.add_argument(
        "--collection"
    )

    parser.add_argument(
        "--max-chars",
        type=int,
        default=1600,
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=16,
    )

    parser.add_argument(
        "--no-pull",
        action="store_true",
    )

    args = parser.parse_args()

    try:
        import chromadb

    except ImportError as exc:
        raise RuntimeError(
            (
                "chromadb is missing. "
                "Install it using "
                "pip install chromadb"
            )
        ) from exc

    project_dir = Path(
        args.project_dir
    ).resolve()

    if args.markdown:
        markdown_path = Path(args.markdown).resolve()
    else:
        markdown_path = project_dir / "manual_sections" / "overall.md"
        if not markdown_path.is_file():
            markdown_path = project_dir / "manual.md"  # older projects

    if not markdown_path.is_file():
        raise RuntimeError(
            (
                "Manual Markdown not found: "
                f"{markdown_path}"
            )
        )

    if args.batch_size < 1:
        raise RuntimeError(
            "batch size must be at least 1"
        )

    if not args.no_pull:
        pull_model(
            args.model
        )

    markdown = markdown_path.read_text(
        encoding="utf-8"
    )

    if not markdown.strip():
        raise RuntimeError(
            "Manual Markdown is empty"
        )

    chunks = split_manual(
        markdown,
        args.max_chars,
    )

    print(
        (
            f"Created {len(chunks)} "
            "task aware chunks"
        )
    )

    source_sha256 = sha256_text(
        markdown
    )

    source_id = sha256_text(
        (
            f"{project_dir.name}|"
            f"{markdown_path}"
        )
    )

    collection_name = (
        safe_collection_name(
            args.collection
            or (
                f"{project_dir.name}_"
                f"{args.model}_manual"
            )
        )
    )

    analysis_dir = (
        project_dir
        / "pdf_analysis"
    )

    analysis_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    chroma_path = (
        analysis_dir
        / "chroma_db"
    )

    started = time.perf_counter()

    embeddings = []

    for start in range(
        0,
        len(chunks),
        args.batch_size,
    ):
        batch = chunks[
            start:
            start + args.batch_size
        ]

        embeddings.extend(
            ollama_embed(
                args.ollama_url,
                args.model,
                [
                    item["text"]
                    for item in batch
                ],
            )
        )

        print(
            (
                f"Embedded "
                f"{min(start + len(batch), len(chunks))}"
                f"/{len(chunks)} chunks"
            )
        )

    dimension, norm = (
        validate_embeddings(
            embeddings
        )
    )

    client = chromadb.PersistentClient(
        path=str(chroma_path)
    )

    try:
        old = client.get_collection(
            name=collection_name,
            embedding_function=None,
        )

        previous_count = old.count()

        client.delete_collection(
            name=collection_name
        )

        reset = True

    except Exception:
        previous_count = 0
        reset = False

    collection = client.create_collection(
        name=collection_name,
        embedding_function=None,
        metadata={
            "hnsw:space": "cosine",
            "embedding_model": (
                args.model
            ),
            "project": (
                project_dir.name
            ),
            "latest_source_sha256": (
                source_sha256
            ),
        },
    )

    indexed_at = datetime.now(
        timezone.utc
    ).isoformat()

    source_info = {
        "project": project_dir.name,
        "source": markdown_path.name,
        "source_id": source_id,
        "source_sha256": (
            source_sha256
        ),
        "model": args.model,
    }

    ids = []
    metadatas = []
    documents = []
    manifest = []

    for index, chunk in enumerate(
        chunks
    ):
        chunk_hash = sha256_text(
            chunk["text"]
        )

        record_id = sha256_text(
            (
                f"{source_sha256}|"
                f"{chunk['task_id']}|"
                f"{chunk['part_index']}|"
                f"{chunk_hash}"
            )
        )

        metadata = scalar_metadata(
            chunk,
            source_info,
            indexed_at,
        )

        metadata["chunk_sha256"] = (
            chunk_hash
        )

        ids.append(
            record_id
        )

        metadatas.append(
            metadata
        )

        documents.append(
            chunk["text"]
        )

        manifest.append(
            {
                "id": record_id,
                "metadata": metadata,
                "preview": (
                    chunk["text"][:400]
                ),
            }
        )

    collection.upsert(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas,
    )

    current_count = (
        collection.count()
    )

    if current_count != len(chunks):
        raise RuntimeError(
            (
                "Index verification failed. "
                f"Expected {len(chunks)} records, "
                f"found {current_count}"
            )
        )

    report = {
        "source": str(
            markdown_path
        ),
        "source_sha256": (
            source_sha256
        ),
        "collection": (
            collection_name
        ),
        "collection_reset": reset,
        "previous_record_count": (
            previous_count
        ),
        "chunk_count": len(chunks),
        "collection_count": (
            current_count
        ),
        "stale_record_count": 0,
        "embedding_model": (
            args.model
        ),
        "embedding_dimension": (
            dimension
        ),
        "first_vector_l2_norm": (
            norm
        ),
        "max_chars": (
            args.max_chars
        ),
        "elapsed_seconds": round(
            time.perf_counter()
            - started,
            3,
        ),
        "chroma_path": str(
            chroma_path
        ),
    }

    (
        analysis_dir
        / "embedding_report.json"
    ).write_text(
        json.dumps(
            report,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    (
        analysis_dir
        / "chunk_manifest.json"
    ).write_text(
        json.dumps(
            manifest,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    readme = f"""# Embedding Index Report

| Field | Value |
|---|---|
| Source | `{markdown_path}` |
| Collection | `{collection_name}` |
| Collection reset | {reset} |
| Previous records | {previous_count} |
| Task aware chunks | {len(chunks)} |
| Current records | {current_count} |
| Stale records | 0 |
| Embedding model | `{args.model}` |
| Embedding dimension | {dimension} |
| First vector L2 norm | {norm:.8f} |
| Chunk size | {args.max_chars} |
| Chroma path | `{chroma_path}` |

The chunk details are available in `chunk_manifest.json`.
"""

    (
        analysis_dir
        / "EMBEDDING_README.md"
    ).write_text(
        readme,
        encoding="utf-8",
    )

    print(
        f"Collection: {collection_name}"
    )

    print(
        f"Current records: {current_count}"
    )

    print(
        "Stale records: 0"
    )


if __name__ == "__main__":
    try:
        main()

    except (
        RuntimeError,
        subprocess.CalledProcessError,
    ) as exc:
        print(
            f"ERROR: {exc}",
            file=sys.stderr,
        )

        raise SystemExit(1)