# Tasks: RAG Agent

**Input**: Design documents from `/specs/003-rag-agent/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Install `openai` Python dependency in `backend/pyproject.toml` using `uv`
- [x] T002 Verify `OPENAI_API_KEY` exists in `.env` and `backend/.env` (if applicable)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure for agent

- [x] T003 Create `backend/tests/test_agent.py` with mock fixtures for OpenAI client and `retrieve.py`
- [x] T004 Create `backend/agent.py` skeleton with `click` groups and basic logging setup
- [x] T005 [P] Implement `search_knowledge_base` tool function wrapper in `backend/agent.py` importing `backend.retrieve`

**Checkpoint**: Foundation ready - user story implementation can begin

---

## Phase 3: User Story 1 - Agent Initialization (Priority: P1)

**Goal**: Initialize the OpenAI Agent with the correct tools.

**Independent Test**: Run `uv run agent.py init` (internal debug command) or verify via unit test that the agent is created with tools.

### Tests for User Story 1

- [x] T006 [P] [US1] Unit test for Agent initialization (OpenAI client creation) in `backend/tests/test_agent.py`
- [x] T007 [P] [US1] Unit test for Tool schema generation (JSON format) in `backend/tests/test_agent.py`

### Implementation for User Story 1

- [x] T008 [US1] Implement `create_assistant` function in `backend/agent.py` (or reuse existing assistant by ID if stored)
- [x] T009 [US1] Configure the "Retrieval Tool" definition (JSON schema) passed to the OpenAI Assistant
- [x] T010 [US1] Add logic to persist/load `assistant_id` to avoid creating duplicates (optional: use a fixed name or env var)

**Checkpoint**: User Story 1 (Initialization) functional.

---

## Phase 4: User Story 2 - Question Answering with Retrieval (Priority: P1)

**Goal**: Answer questions using retrieved content.

**Independent Test**: Run `uv run agent.py ask "Docusaurus"` and check output.

### Tests for User Story 2

- [x] T011 [P] [US2] Unit test for `ask` command: Verify `run.submit_tool_outputs` flow in `backend/tests/test_agent.py`
- [x] T012 [P] [US2] Unit test for handling run status (queued, in_progress, requires_action, completed) in `backend/tests/test_agent.py`

### Implementation for User Story 2

- [x] T013 [US2] Implement `process_message` loop in `backend/agent.py` (Create Thread -> Add Message -> Run -> Poll Status -> Handle Tool Calls)
- [x] T014 [US2] Implement tool execution logic: Call `perform_search` when the API requests `search_knowledge_base`
- [x] T015 [US2] Implement `ask` command in `backend/agent.py` CLI to trigger the flow
- [x] T016 [US2] Format the final response to stdout

**Checkpoint**: User Story 2 (Q&A) functional.

---

## Phase 5: User Story 3 - Follow-up Context (Priority: P2)

**Goal**: Support conversation history via Threads.

**Independent Test**: Run `uv run agent.py chat` and ask two related questions.

### Tests for User Story 3

- [x] T017 [P] [US3] Unit test for Thread persistence (mocking the ID reuse) in `backend/tests/test_agent.py`

### Implementation for User Story 3

- [x] T018 [US3] Implement `chat` command in `backend/agent.py` for interactive session loop
- [x] T019 [US3] Add support for `--thread-id` in CLI to resume previous conversations (optional but good for testing)

**Checkpoint**: User Story 3 (Context) functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

- [x] T020 [P] Update `specs/003-rag-agent/quickstart.md` with final usage examples
- [x] T021 Refine error handling for OpenAI API timeouts or Qdrant connection failures in `backend/agent.py`
- [x] T022 Final code cleanup and type hint verification

---

## Dependencies & Execution Order

- **Phase 1 & 2**: Prerequisites for all code.
- **Phase 3**: Sets up the Agent/Assistant entity.
- **Phase 4**: Implements the core run loop and tool handling.
- **Phase 5**: Adds statefulness (Threads) and interactive mode.
- **Phase 6**: Final cleanup.

## Implementation Strategy

- **MVP**: Complete Phase 1-4 to get a single-turn Question-Answer bot.
- **Incremental**: Add Phase 5 for multi-turn chat.
