# Tasks: RAG Retrieval Validation

**Input**: Design documents from `/specs/002-rag-retrieval-validation/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 [P] Ensure `backend/` directory exists and `uv` is configured (Reference Plan)
- [x] T002 Verify `.env` contains `QDRANT_URL`, `QDRANT_API_KEY`, and `COHERE_API_KEY` (Reference Spec-1 setup)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure for validation

- [x] T003 Create `backend/tests/test_retrieve.py` with mock fixtures for Qdrant and HTTP requests
- [x] T004 Define `RetrievalResult` and `ValidationReport` data classes in `backend/retrieve.py` (Draft)

**Checkpoint**: Foundation ready - user story implementation can begin

---

## Phase 3: User Story 1 - Search Document Content (Priority: P1) 🎯 MVP

**Goal**: Implement natural language search against existing embeddings.

**Independent Test**: Run `uv run retrieve.py "query" --no-validate` and see top-k results.

### Tests for User Story 1

- [x] T005 [P] [US1] Unit test for similarity search logic in `backend/tests/test_retrieve.py` (Verify `query_points` call)
- [x] T006 [P] [US1] Unit test for search result formatting in `backend/tests/test_retrieve.py`

### Implementation for User Story 1

- [x] T007 [P] [US1] Implement search logic using `client.query_points` in `backend/retrieve.py`
- [x] T008 [US1] Implement result formatting (Score, Title, URL, Text) in `backend/retrieve.py`
- [x] T009 [US1] Add `click` CLI interface for the search query and `--limit` option

**Checkpoint**: User Story 1 (Retrieval) functional and testable.

---

## Phase 4: User Story 2 - Verify Metadata Integrity (Priority: P2)

**Goal**: Validate reachability of source URLs in retrieved chunks.

**Independent Test**: Run `uv run retrieve.py "query"` and see "Valid URLs: X/X" in the report.

### Tests for User Story 2

- [x] T010 [P] [US2] Unit test for URL reachability check in `backend/tests/test_retrieve.py` (Mock `httpx`)

### Implementation for User Story 2

- [x] T011 [US2] Implement HTTP HEAD request check for metadata URLs in `backend/retrieve.py`
- [x] T012 [US2] Add validation status reporting (PASS/FAIL) to the CLI output
- [x] T013 [US2] Implement `--validate/--no-validate` toggle

**Checkpoint**: User Story 2 (Integrity) functional.

---

## Phase 5: Polish & Cross-Cutting Concerns

- [x] T014 [P] Update `specs/002-rag-retrieval-validation/quickstart.md` with final command examples
- [x] T015 Run `uv run retrieve.py` against a known topic from the documentation
- [x] T016 Final code cleanup and type hint verification in `retrieve.py`

---

## Dependencies & Execution Order

- **Setup (Phase 1)**: Start immediately.
- **Foundational (Phase 2)**: Depends on Phase 1.
- **User Stories (Phase 3 & 4)**: US1 must be complete for search; US2 adds validation layer to US1 results.
- **Polish (Phase 5)**: Follows all story completions.