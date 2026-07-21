"""Evaluate manual retrieval using a JSON question set."""

import argparse
import json
from pathlib import Path

from ask_manual import (
    ManualRetriever,
    build_query_plan,
)


def matches_expected(
    metadata: dict,
    case: dict,
) -> bool:
    checks = []

    for case_key, metadata_key in [
        (
            "expected_module",
            "module",
        ),
        (
            "expected_page",
            "page",
        ),
        (
            "expected_task",
            "task",
        ),
    ]:
        expected = str(
            case.get(case_key)
            or ""
        ).strip().lower()

        if expected:
            actual = str(
                metadata.get(
                    metadata_key
                )
                or ""
            ).strip().lower()

            checks.append(
                expected in actual
                or actual in expected
            )

    return (
        all(checks)
        if checks
        else False
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__
    )

    parser.add_argument(
        "project_dir"
    )

    parser.add_argument(
        "questions_json"
    )

    parser.add_argument(
        "--embedding-model",
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
        "--gemini-model",
        default="gemini-3.1-flash-lite",
    )

    parser.add_argument(
        "--no-llm-expansion",
        action="store_true",
    )

    args = parser.parse_args()

    cases = json.loads(
        Path(
            args.questions_json
        ).read_text(
            encoding="utf-8"
        )
    )

    if (
        not isinstance(
            cases,
            list,
        )
        or not cases
    ):
        raise RuntimeError(
            (
                "Question file must contain "
                "a nonempty JSON array"
            )
        )

    retriever = ManualRetriever(
        project_dir=Path(
            args.project_dir
        ),
        embedding_model=(
            args.embedding_model
        ),
        ollama_url=(
            args.ollama_url
        ),
        collection_name=(
            args.collection
        ),
    )

    results = []

    top1 = 0
    top3 = 0
    top5 = 0

    for case in cases:
        question = case[
            "question"
        ]

        plan = build_query_plan(
            question,
            not args.no_llm_expansion,
            args.gemini_model,
        )

        chunks = retriever.retrieve(
            question,
            plan,
            final_top_k=5,
        )

        unique_tasks = []
        seen = set()

        for chunk in chunks:
            task_id = chunk.metadata.get(
                "task_id"
            )

            if task_id in seen:
                continue

            seen.add(
                task_id
            )

            unique_tasks.append(
                chunk
            )

        ranks = [
            index
            for index, chunk in enumerate(
                unique_tasks[:5],
                start=1,
            )
            if matches_expected(
                chunk.metadata,
                case,
            )
        ]

        first_rank = (
            min(ranks)
            if ranks
            else None
        )

        top1 += int(
            first_rank == 1
        )

        top3 += int(
            first_rank is not None
            and first_rank <= 3
        )

        top5 += int(
            first_rank is not None
            and first_rank <= 5
        )

        results.append(
            {
                **case,
                "matched_rank": (
                    first_rank
                ),
                "retrieved": [
                    {
                        "module": (
                            chunk.metadata.get(
                                "module"
                            )
                        ),
                        "page": (
                            chunk.metadata.get(
                                "page"
                            )
                        ),
                        "task": (
                            chunk.metadata.get(
                                "task"
                            )
                        ),
                        "score": (
                            chunk.score
                        ),
                        "confidence": (
                            chunk.confidence
                        ),
                    }
                    for chunk in unique_tasks[
                        :5
                    ]
                ],
            }
        )

        print(
            (
                f"Question: {question} "
                f"| rank: {first_rank}"
            )
        )

    total = len(
        cases
    )

    summary = {
        "total_questions": total,
        "top1_accuracy": (
            top1 / total
        ),
        "top3_accuracy": (
            top3 / total
        ),
        "top5_accuracy": (
            top5 / total
        ),
        "results": results,
    }

    output_path = (
        Path(args.project_dir)
        / "pdf_analysis"
        / "retrieval_evaluation.json"
    )

    output_path.write_text(
        json.dumps(
            summary,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        (
            "Top 1 accuracy: "
            f"{summary['top1_accuracy']:.3f}"
        )
    )

    print(
        (
            "Top 3 accuracy: "
            f"{summary['top3_accuracy']:.3f}"
        )
    )

    print(
        (
            "Top 5 accuracy: "
            f"{summary['top5_accuracy']:.3f}"
        )
    )

    print(
        f"Report: {output_path}"
    )


if __name__ == "__main__":
    try:
        main()

    except RuntimeError as exc:
        print(
            f"ERROR: {exc}"
        )

        raise SystemExit(1)