# Tasks: Book Content Ingestion & Embedding

**Input**: Design documents from `/specs/001-book-rag-ingestion/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure: `backend/`, `backend/tests/`
- [x] T002 Initialize Python project with `uv init backend` and add dependencies (`cohere`, `qdrant-client`, `httpx`, `beautifulsoup4`, `click`, `python-dotenv`, `pytest`)
- [x] T003 [P] Configure `.env.example` and `.gitignore` for the backend project

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure for environment and logging

- [x] T004 Implement configuration loader for environment variables in `backend/storage.py` (placeholder for Qdrant setup)
- [x] T005 [P] Setup basic logging configuration in `backend/main.py`
- [x] T006 Create `backend/tests/conftest.py` with mock fixtures for Cohere and Qdrant

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Ingest Documentation Site (Priority: P1) 🎯 MVP

**Goal**: Crawl Docusaurus sitemap, extract text, embed, and store in Qdrant.

**Independent Test**: Run `uv run main.py ingest <URL>` and verify the process completes with indexed points in Qdrant.

### Tests for User Story 1

- [x] T007 [P] [US1] Unit test for sitemap parsing and URL extraction in `backend/tests/test_crawler.py`
- [x] T008 [P] [US1] Unit test for HTML text extraction and cleaning (BS4) in `backend/tests/test_crawler.py`
- [x] T009 [P] [US1] Unit test for text chunking logic in `backend/tests/test_processor.py`

### Implementation for User Story 1

- [x] T010 [P] [US1] Implement `backend/crawler.py` for sitemap fetching and HTML cleaning
- [x] T011 [P] [US1] Implement `backend/processor.py` for text chunking and Cohere embedding generation
- [x] T012 [P] [US1] Implement `backend/storage.py` for Qdrant collection creation and point upsertion
- [x] T013 [US1] Implement `ingest` command in `backend/main.py` using `click`
- [x] T014 [US1] Add rate limiting retry logic for Cohere/Qdrant calls in `processor.py` and `storage.py`

**Checkpoint**: User Story 1 (Ingestion) functional and testable.

---

## Phase 4: User Story 2 - Verify Embeddings via Search (Priority: P1)

**Goal**: Perform similarity search against Qdrant using the CLI.

**Independent Test**: Run `uv run main.py search "query"` and verify relevant text chunks are returned.

### Tests for User Story 2

- [x] T015 [P] [US2] Unit test for similarity search result parsing in `backend/tests/test_storage.py`

### Implementation for User Story 2

- [x] T016 [US2] Implement `search` function in `backend/storage.py`
- [x] T017 [US2] Implement `search` command in `backend/main.py` using `click`
- [x] T018 [US2] Add result formatting for CLI output (title, URL, chunk text)

**Checkpoint**: User Story 2 (Search) functional.

---

## Phase 5: Polish & Cross-Cutting Concerns

- [x] T019 [P] Update `backend/README.md` with usage examples
- [x] T020 Run `uv run main.py` validation against the deployed Vercel URL
- [x] T021 Final code cleanup and type hint verification

---

## Dependencies & Execution Order

- **Setup (Phase 1)**: Start immediately.
- **Foundational (Phase 2)**: Depends on Phase 1.
- **User Stories (Phase 3 & 4)**: Can run in parallel after Phase 2, but P1 Ingestion is usually required for P1 Search verification.
- **Polish (Phase 5)**: Follows all story completions.
