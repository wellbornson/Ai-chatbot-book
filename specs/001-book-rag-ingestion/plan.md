# Implementation Plan: URL Ingestion & Embedding Pipeline

**Branch**: `001-book-rag-ingestion` | **Date**: 2025-12-24 | **Spec**: [specs/001-book-rag-ingestion/spec.md](spec.md)
**Input**: Feature specification from `/specs/001-book-rag-ingestion/spec.md`

## Summary

Build a Python-based ETL pipeline that crawls a Docusaurus documentation site, cleans the text, generates vector embeddings using Cohere, and stores them in Qdrant Cloud. The system will be managed using `uv` and provide a CLI for both ingestion and testing queries.

## Technical Context

**Language/Version**: Python 3.12+ (managed via `uv`)
**Primary Dependencies**: `cohere`, `qdrant-client`, `httpx`, `beautifulsoup4`, `click` (for CLI), `python-dotenv`
**Storage**: Qdrant Cloud (Free Tier)
**Testing**: `pytest`
**Target Platform**: CLI / Python Script
**Project Type**: Single backend module (`backend/`)
**Performance Goals**: Process 100+ pages in under 5 minutes; search latency < 500ms
**Constraints**: Cohere/Qdrant API rate limits; Cloud Free Tier limits
**Scale/Scope**: Target documentation sites with < 1000 pages

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Spec-First**: Feature specification is complete and validated.
- [x] **Smallest Viable Diff**: Modular script approach ensures minimal footprint.
- [x] **CLI-First**: Requirement FR-006/FR-007 explicitly mandate CLI interfaces.
- [x] **Testable**: Independent tests defined for both ingestion and search.

## Project Structure

### Documentation (this feature)

```text
specs/001-book-rag-ingestion/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── checklists/
│   └── requirements.md  # Spec validation
└── tasks.md             # Phase 2 output (to be created)
```

### Source Code (repository root)

```text
backend/
├── pyproject.toml       # uv managed dependencies
├── .env                 # Environment variables (API keys)
├── main.py              # Main entry point (crawling, embedding, storage)
├── crawler.py           # Site crawling and text extraction
├── processor.py         # Text chunking and embedding logic
├── storage.py           # Qdrant integration
└── tests/
    ├── conftest.py
    ├── test_crawler.py
    ├── test_processor.py
    └── test_storage.py
```

**Structure Decision**: Option 2: Web application (Backend-only focus). A `backend/` directory will contain the Python project, isolated from the root Docusaurus files.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |