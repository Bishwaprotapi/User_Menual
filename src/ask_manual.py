"""Ask questions against a manual using hybrid retrieval and grounded answers."""

import argparse
import json
import math
import os
import re
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

TOKEN_RE = re.compile(
    r"[\w]+",
    re.UNICODE,
)

ACTION_WORDS = {
    "create": {
        "create",
        "add",
        "register",
        "new",
        "insert",
        "তৈরি",
        "যোগ",
        "করবো",
        "korbo",
    },
    "edit": {
        "edit",
        "update",
        "change",
        "modify",
        "পরিবর্তন",
        "আপডেট",
    },
    "view": {
        "view",
        "show",
        "details",
        "see",
        "দেখ",
        "dekho",
    },
    "search": {
        "search",
        "find",
        "look",
        "খুঁজ",
    },
    "filter": {
        "filter",
        "sort",
        "ফিল্টার",
        "বাছাই",
    },
    "approve": {
        "approve",
        "accept",
        "অনুমোদন",
    },
    "export": {
        "export",
        "download",
        "report",
        "ডাউনলোড",
        "রিপোর্ট",
    },
    "configure": {
        "configure",
        "setup",
        "setting",
        "settings",
        "কনফিগার",
        "সেটিং",
    },
}

SYNONYM_GROUPS = [
    {
        "employee",
        "staff",
        "worker",
        "কর্মচারী",
        "স্টাফ",
    },
    {
        "create",
        "add",
        "register",
        "insert",
        "new",
        "তৈরি",
        "যোগ",
    },
    {
        "edit",
        "update",
        "change",
        "modify",
        "পরিবর্তন",
        "আপডেট",
    },
    {
        "view",
        "show",
        "details",
        "see",
        "দেখা",
    },
    {
        "leave",
        "holiday",
        "absence",
        "ছুটি",
    },
    {
        "role",
        "permission",
        "access",
        "অনুমতি",
    },
    {
        "report",
        "export",
        "download",
        "রিপোর্ট",
        "ডাউনলোড",
    },
]


def tokenize(
    text: str,
) -> list[str]:
    return [
        token.lower()
        for token in TOKEN_RE.findall(
            text
        )
    ]


def normalize_space(
    text: str,
) -> str:
    return re.sub(
        r"\s+",
        " ",
        text,
    ).strip()


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

    vectors = result.get(
        "embeddings",
        [],
    )

    if len(vectors) != len(texts):
        raise RuntimeError(
            (
                "Ollama returned an unexpected "
                "number of embeddings"
            )
        )

    return vectors


def local_query_plan(
    question: str,
) -> dict:
    normalized = normalize_space(
        question
    )

    tokens = set(
        tokenize(normalized)
    )

    expanded_terms = set(
        tokens
    )

    for group in SYNONYM_GROUPS:
        if tokens.intersection(
            group
        ):
            expanded_terms.update(
                group
            )

    action = "other"

    for action_name, words in (
        ACTION_WORDS.items()
    ):
        if tokens.intersection(
            words
        ):
            action = action_name
            break

    expansions = [
        normalized
    ]

    if expanded_terms != tokens:
        expansions.append(
            " ".join(
                sorted(expanded_terms)
            )
        )

    return {
        "normalized_question": (
            normalized
        ),
        "language": "unknown",
        "intent": action,
        "module_hint": "",
        "role_hint": "",
        "expansions": (
            expansions[:4]
        ),
    }


def gemini_query_plan(
    question: str,
    model: str,
) -> dict:
    from google import genai
    from google.genai import types

    client = genai.Client()

    prompt = f"""Normalize this software manual question and create search variants.
Return JSON only with these fields:
normalized_question, language, intent, module_hint, role_hint, expansions.
Intent must be one of create, edit, view, search, filter, approve, export, configure, or other.
Expansions must contain at most four short questions or phrases and preserve the original meaning.
Support Bangla, English, and Bangla English mixed writing.

Question: {question}
"""

    response = (
        client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type=(
                    "application/json"
                ),
                max_output_tokens=1024,
            ),
        )
    )

    return json.loads(
        response.text
    )


def build_query_plan(
    question: str,
    use_llm: bool,
    gemini_model: str,
) -> dict:
    base = local_query_plan(
        question
    )

    if not use_llm:
        return base

    try:
        llm_plan = gemini_query_plan(
            question,
            gemini_model,
        )

        expansions = [
            question,
            llm_plan.get(
                "normalized_question",
                "",
            ),
        ]

        expansions.extend(
            llm_plan.get(
                "expansions"
            )
            or []
        )

        deduplicated = []
        seen = set()

        for item in expansions:
            item = normalize_space(
                str(item)
            )

            key = item.lower()

            if item and key not in seen:
                seen.add(
                    key
                )

                deduplicated.append(
                    item
                )

        llm_plan["expansions"] = (
            deduplicated[:5]
        )

        return {
            **base,
            **llm_plan,
        }

    except Exception as exc:
        print(
            (
                "Query expansion fallback used: "
                f"{exc}"
            )
        )

        return base


def bm25_scores(
    documents: list[str],
    query: str,
    k1: float = 1.5,
    b: float = 0.75,
) -> list[float]:
    tokenized_docs = [
        tokenize(document)
        for document in documents
    ]

    query_tokens = tokenize(
        query
    )

    if (
        not query_tokens
        or not tokenized_docs
    ):
        return [
            0.0
        ] * len(documents)

    document_count = len(
        tokenized_docs
    )

    average_length = (
        sum(
            len(tokens)
            for tokens in tokenized_docs
        )
        / max(
            document_count,
            1,
        )
    )

    document_frequency = Counter()

    for tokens in tokenized_docs:
        for token in set(tokens):
            document_frequency[
                token
            ] += 1

    scores = []

    for tokens in tokenized_docs:
        frequencies = Counter(
            tokens
        )

        score = 0.0
        length = len(tokens)

        for token in query_tokens:
            df = document_frequency.get(
                token,
                0,
            )

            if df == 0:
                continue

            idf = math.log(
                1
                + (
                    document_count
                    - df
                    + 0.5
                )
                / (
                    df
                    + 0.5
                )
            )

            frequency = frequencies.get(
                token,
                0,
            )

            denominator = (
                frequency
                + k1
                * (
                    1
                    - b
                    + b
                    * length
                    / max(
                        average_length,
                        1,
                    )
                )
            )

            if denominator:
                score += (
                    idf
                    * frequency
                    * (
                        k1
                        + 1
                    )
                    / denominator
                )

        scores.append(
            score
        )

    return scores


def lexical_overlap(
    question: str,
    text: str,
) -> float:
    query_tokens = set(
        tokenize(question)
    )

    if not query_tokens:
        return 0.0

    text_tokens = set(
        tokenize(text)
    )

    return (
        len(
            query_tokens.intersection(
                text_tokens
            )
        )
        / len(query_tokens)
    )


def detect_action(
    question: str,
) -> str:
    tokens = set(
        tokenize(question)
    )

    for action, words in (
        ACTION_WORDS.items()
    ):
        if tokens.intersection(
            words
        ):
            return action

    return "other"


def reciprocal_rank_fusion(
    rankings: list[list[str]],
    constant: int = 60,
) -> dict[str, float]:
    scores = defaultdict(
        float
    )

    for ranking in rankings:
        for rank, item_id in enumerate(
            ranking,
            start=1,
        ):
            scores[item_id] += (
                1.0
                / (
                    constant
                    + rank
                )
            )

    return dict(
        scores
    )


@dataclass
class RetrievedChunk:
    record_id: str
    document: str
    metadata: dict
    score: float
    confidence: float
    vector_similarity: float
    lexical_score: float


class ManualRetriever:
    def __init__(
        self,
        project_dir: Path,
        embedding_model: str = (
            "qwen3-embedding:0.6b"
        ),
        ollama_url: str = (
            "http://localhost:11434"
        ),
        collection_name: str | None = None,
    ):
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

        self.project_dir = (
            project_dir.resolve()
        )

        self.embedding_model = (
            embedding_model
        )

        self.ollama_url = (
            ollama_url
        )

        self.collection_name = (
            collection_name
            or self.safe_collection_name(
                (
                    f"{self.project_dir.name}_"
                    f"{embedding_model}_manual"
                )
            )
        )

        self.chroma_path = (
            self.project_dir
            / "pdf_analysis"
            / "chroma_db"
        )

        self.client = (
            chromadb.PersistentClient(
                path=str(
                    self.chroma_path
                )
            )
        )

        self.collection = (
            self.client.get_collection(
                name=self.collection_name,
                embedding_function=None,
            )
        )

        stored_model = (
            self.collection.metadata
            or {}
        ).get(
            "embedding_model"
        )

        if (
            stored_model
            and stored_model
            != embedding_model
        ):
            raise RuntimeError(
                (
                    f"Collection uses {stored_model}, "
                    f"but the query requested "
                    f"{embedding_model}"
                )
            )

        records = (
            self.collection.get(
                include=[
                    "documents",
                    "metadatas",
                ]
            )
        )

        self.ids = records.get(
            "ids",
            [],
        )

        self.documents = records.get(
            "documents",
            [],
        )

        self.metadatas = records.get(
            "metadatas",
            [],
        )

        self.by_id = {
            record_id: {
                "document": document,
                "metadata": metadata,
            }
            for (
                record_id,
                document,
                metadata,
            ) in zip(
                self.ids,
                self.documents,
                self.metadatas,
            )
        }

        self.index_by_id = {
            record_id: index
            for index, record_id in enumerate(
                self.ids
            )
        }

    @staticmethod
    def safe_collection_name(
        value: str,
    ) -> str:
        cleaned = re.sub(
            r"[^a-zA-Z0-9._-]+",
            "_",
            value,
        ).strip("._-")

        return cleaned[:200]

    def retrieve(
        self,
        question: str,
        query_plan: dict,
        vector_top_k: int = 20,
        keyword_top_k: int = 20,
        final_top_k: int = 5,
    ) -> list[RetrievedChunk]:
        expansions = (
            query_plan.get(
                "expansions"
            )
            or [
                question
            ]
        )

        embeddings = ollama_embed(
            self.ollama_url,
            self.embedding_model,
            expansions,
        )

        vector_rankings = []

        vector_similarity = defaultdict(
            float
        )

        for expansion, vector in zip(
            expansions,
            embeddings,
        ):
            results = (
                self.collection.query(
                    query_embeddings=[
                        vector
                    ],
                    n_results=min(
                        vector_top_k,
                        len(self.ids),
                    ),
                    include=[
                        "documents",
                        "metadatas",
                        "distances",
                    ],
                )
            )

            ranking = results.get(
                "ids",
                [[]],
            )[0]

            distances = results.get(
                "distances",
                [[]],
            )[0]

            vector_rankings.append(
                ranking
            )

            for record_id, distance in zip(
                ranking,
                distances,
            ):
                similarity = max(
                    0.0,
                    1.0
                    - float(distance),
                )

                vector_similarity[
                    record_id
                ] = max(
                    vector_similarity[
                        record_id
                    ],
                    similarity,
                )

        combined_query = " ".join(
            expansions
        )

        bm25 = bm25_scores(
            self.documents,
            combined_query,
        )

        keyword_indices = sorted(
            range(len(bm25)),
            key=lambda index: bm25[
                index
            ],
            reverse=True,
        )

        keyword_indices = [
            index
            for index in keyword_indices
            if bm25[index] > 0
        ][:keyword_top_k]

        keyword_ranking = [
            self.ids[index]
            for index in keyword_indices
        ]

        rrf = reciprocal_rank_fusion(
            [
                *vector_rankings,
                keyword_ranking,
            ]
        )

        max_bm25 = (
            max(bm25)
            if bm25
            else 0.0
        )

        requested_action = (
            query_plan.get("intent")
            or detect_action(
                question
            )
        )

        module_hint = str(
            query_plan.get(
                "module_hint"
            )
            or ""
        ).lower()

        role_hint = str(
            query_plan.get(
                "role_hint"
            )
            or ""
        ).lower()

        candidates = set(
            rrf
        )

        scored = []

        for record_id in candidates:
            item = self.by_id.get(
                record_id
            )

            if not item:
                continue

            document = item[
                "document"
            ]

            metadata = item[
                "metadata"
            ]

            doc_index = (
                self.index_by_id[
                    record_id
                ]
            )

            lexical = lexical_overlap(
                combined_query,
                document,
            )

            keyword_normalized = (
                bm25[doc_index]
                / max_bm25
                if max_bm25 > 0
                else 0.0
            )

            heading_text = " ".join(
                [
                    str(
                        metadata.get(
                            "module",
                            "",
                        )
                    ),
                    str(
                        metadata.get(
                            "page",
                            "",
                        )
                    ),
                    str(
                        metadata.get(
                            "task",
                            "",
                        )
                    ),
                    str(
                        metadata.get(
                            "keywords_json",
                            "",
                        )
                    ),
                ]
            )

            heading_overlap = (
                lexical_overlap(
                    combined_query,
                    heading_text,
                )
            )

            phrase_boost = (
                1.0
                if normalize_space(
                    question
                ).lower()
                in document.lower()
                else 0.0
            )

            action_boost = (
                1.0
                if (
                    requested_action
                    != "other"
                    and metadata.get(
                        "action"
                    )
                    == requested_action
                )
                else 0.0
            )

            module_boost = (
                1.0
                if (
                    module_hint
                    and module_hint
                    in str(
                        metadata.get(
                            "module",
                            "",
                        )
                    ).lower()
                )
                else 0.0
            )

            role_boost = (
                1.0
                if (
                    role_hint
                    and role_hint
                    in str(
                        metadata.get(
                            "roles_json",
                            "",
                        )
                    ).lower()
                )
                else 0.0
            )

            base_rrf = rrf.get(
                record_id,
                0.0,
            )

            score = (
                base_rrf
                * 8.0
                + vector_similarity.get(
                    record_id,
                    0.0,
                )
                * 0.34
                + keyword_normalized
                * 0.20
                + lexical
                * 0.16
                + heading_overlap
                * 0.14
                + phrase_boost
                * 0.04
                + action_boost
                * 0.07
                + module_boost
                * 0.03
                + role_boost
                * 0.02
            )

            confidence = min(
                1.0,
                vector_similarity.get(
                    record_id,
                    0.0,
                )
                * 0.52
                + lexical
                * 0.20
                + heading_overlap
                * 0.16
                + keyword_normalized
                * 0.08
                + action_boost
                * 0.04,
            )

            scored.append(
                RetrievedChunk(
                    record_id=record_id,
                    document=document,
                    metadata=metadata,
                    score=score,
                    confidence=confidence,
                    vector_similarity=(
                        vector_similarity.get(
                            record_id,
                            0.0,
                        )
                    ),
                    lexical_score=(
                        lexical
                    ),
                )
            )

        scored.sort(
            key=lambda item: item.score,
            reverse=True,
        )

        selected = scored[
            :final_top_k
        ]

        return self.expand_same_task(
            selected
        )

    def expand_same_task(
        self,
        selected: list[RetrievedChunk],
    ) -> list[RetrievedChunk]:
        selected_ids = {
            item.record_id
            for item in selected
        }

        expanded = list(
            selected
        )

        task_ids = {
            item.metadata.get(
                "task_id"
            )
            for item in selected
            if item.metadata.get(
                "task_id"
            )
        }

        for (
            record_id,
            document,
            metadata,
        ) in zip(
            self.ids,
            self.documents,
            self.metadatas,
        ):
            if (
                record_id in selected_ids
                or metadata.get(
                    "task_id"
                )
                not in task_ids
            ):
                continue

            expanded.append(
                RetrievedChunk(
                    record_id=record_id,
                    document=document,
                    metadata=metadata,
                    score=0.0,
                    confidence=0.0,
                    vector_similarity=0.0,
                    lexical_score=0.0,
                )
            )

        expanded.sort(
            key=lambda item: (
                str(
                    item.metadata.get(
                        "task_id",
                        "",
                    )
                ),
                int(
                    item.metadata.get(
                        "part_index",
                        0,
                    )
                ),
            )
        )

        return expanded


def build_context(
    chunks: list[RetrievedChunk],
) -> tuple[str, list[dict]]:
    context_parts = []
    sources = []

    for index, chunk in enumerate(
        chunks,
        start=1,
    ):
        metadata = (
            chunk.metadata
        )

        try:
            screenshots = json.loads(
                metadata.get(
                    "screenshots_json",
                    "[]",
                )
                or "[]"
            )

        except json.JSONDecodeError:
            screenshots = []

        source = {
            "source_number": index,
            "module": metadata.get(
                "module",
                "",
            ),
            "page": metadata.get(
                "page",
                "",
            ),
            "task": metadata.get(
                "task",
                "",
            ),
            "route": metadata.get(
                "route",
                "",
            ),
            "screenshots": screenshots,
            "confidence": (
                chunk.confidence
            ),
        }

        sources.append(
            source
        )

        context_parts.append(
            (
                f"[Source {index}]\n"
                f"Module: {source['module']}\n"
                f"Page: {source['page']}\n"
                f"Task: {source['task']}\n"
                f"Route: {source['route']}\n"
                f"Content:\n"
                f"{chunk.document}"
            )
        )

    return (
        "\n\n".join(
            context_parts
        ),
        sources,
    )


def gemini_answer(
    question: str,
    context: str,
    model: str,
) -> str:
    from google import genai

    client = genai.Client()

    prompt = f"""Answer the software usage question using only the supplied manual context.

Rules:
1. Do not invent any step, field, permission, button, or result.
2. When the context is insufficient, clearly say that the current manual does not contain enough information.
3. Give direct numbered steps when the context contains a procedure.
4. Mention the module and page.
5. Add source markers such as [Source 1] after supported statements.
6. Answer in the language used by the user.

Question:
{question}

Manual context:
{context}
"""

    response = (
        client.models.generate_content(
            model=model,
            contents=prompt,
        )
    )

    return response.text.strip()


def ollama_answer(
    question: str,
    context: str,
    base_url: str,
    model: str,
) -> str:
    prompt = f"""Answer the software usage question using only the supplied manual context.
Do not invent information. If the context is insufficient, say so clearly.
Use numbered steps when appropriate. Mention the module and page. Add [Source N] markers.
Answer in the language used by the user.

Question:
{question}

Manual context:
{context}
"""

    payload = json.dumps(
        {
            "model": model,
            "stream": False,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a grounded software manual assistant."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        }
    ).encode("utf-8")

    request = urllib.request.Request(
        (
            f"{base_url.rstrip('/')}"
            "/api/chat"
        ),
        data=payload,
        headers={
            "Content-Type": (
                "application/json"
            )
        },
        method="POST",
    )

    with urllib.request.urlopen(
        request,
        timeout=600,
    ) as response:
        result = json.loads(
            response.read().decode(
                "utf-8"
            )
        )

    return result.get(
        "message",
        {},
    ).get(
        "content",
        "",
    ).strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__
    )

    parser.add_argument(
        "project_dir"
    )

    parser.add_argument(
        "question"
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
        "--vector-top-k",
        type=int,
        default=20,
    )

    parser.add_argument(
        "--keyword-top-k",
        type=int,
        default=20,
    )

    parser.add_argument(
        "--final-top-k",
        type=int,
        default=5,
    )

    parser.add_argument(
        "--min-confidence",
        type=float,
        default=0.34,
    )

    parser.add_argument(
        "--no-llm-expansion",
        action="store_true",
    )

    parser.add_argument(
        "--gemini-model",
        default=os.getenv(
            "GEMINI_QUERY_MODEL",
            "gemini-3.1-flash-lite",
        ),
    )

    parser.add_argument(
        "--answer-provider",
        choices=[
            "gemini",
            "ollama",
            "none",
        ],
        default="gemini",
    )

    parser.add_argument(
        "--ollama-chat-model",
        default="qwen3:4b",
    )

    args = parser.parse_args()

    load_dotenv()

    project_dir = Path(
        args.project_dir
    )

    plan = build_query_plan(
        args.question,
        not args.no_llm_expansion,
        args.gemini_model,
    )

    retriever = ManualRetriever(
        project_dir=project_dir,
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

    chunks = retriever.retrieve(
        question=args.question,
        query_plan=plan,
        vector_top_k=(
            args.vector_top_k
        ),
        keyword_top_k=(
            args.keyword_top_k
        ),
        final_top_k=(
            args.final_top_k
        ),
    )

    best_confidence = max(
        (
            chunk.confidence
            for chunk in chunks
        ),
        default=0.0,
    )

    context, sources = build_context(
        chunks
    )

    if (
        not chunks
        or best_confidence
        < args.min_confidence
    ):
        answer = (
            "বর্তমান manual এ এই প্রশ্নের জন্য যথেষ্ট নির্ভরযোগ্য তথ্য পাওয়া যায়নি।"
        )

    elif args.answer_provider == "gemini":
        answer = gemini_answer(
            args.question,
            context,
            args.gemini_model,
        )

    elif args.answer_provider == "ollama":
        answer = ollama_answer(
            args.question,
            context,
            args.ollama_url,
            args.ollama_chat_model,
        )

    else:
        answer = context

    analysis_dir = (
        project_dir
        / "pdf_analysis"
    )

    analysis_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    report = {
        "question": args.question,
        "query_plan": plan,
        "best_confidence": (
            best_confidence
        ),
        "minimum_confidence": (
            args.min_confidence
        ),
        "sources": sources,
        "answer": answer,
    }

    (
        analysis_dir
        / "last_query_report.json"
    ).write_text(
        json.dumps(
            report,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    answer_lines = [
        "# Manual Answer",
        "",
        answer,
        "",
        "## Sources",
        "",
    ]

    for source in sources:
        answer_lines.append(
            (
                f"{source['source_number']}. "
                f"{source['module']} > "
                f"{source['page']} > "
                f"{source['task']}"
            )
        )

        if source["route"]:
            answer_lines.append(
                (
                    "   Route: "
                    f"`{source['route']}`"
                )
            )

        for screenshot in source[
            "screenshots"
        ]:
            answer_lines.append(
                (
                    "   Screenshot: "
                    f"`{screenshot}`"
                )
            )

    (
        analysis_dir
        / "last_answer.md"
    ).write_text(
        "\n".join(
            answer_lines
        ),
        encoding="utf-8",
    )

    print(
        "\nANSWER\n"
    )

    print(
        answer
    )

    print(
        "\nSOURCES\n"
    )

    for source in sources:
        print(
            (
                f"[{source['source_number']}] "
                f"{source['module']} > "
                f"{source['page']} > "
                f"{source['task']}"
            )
        )

    print(
        (
            "\nConfidence: "
            f"{best_confidence:.3f}"
        )
    )


if __name__ == "__main__":
    try:
        main()

    except RuntimeError as exc:
        print(
            f"ERROR: {exc}"
        )

        raise SystemExit(1)