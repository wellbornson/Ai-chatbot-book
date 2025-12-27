# Tasks: Integrate RAG API

**Feature**: `004-integrate-rag-api`
**Plan**: [plan.md](./plan.md)

## Implementation Strategy

We will implement the backend API first to allow manual verification, then build the frontend components and finally wire them together for end-to-end functionality.

## Phase 1: Setup

- [ ] T001 Install backend dependencies `fastapi`, `uvicorn` in `.venv`
- [ ] T002 Verify `backend/agent.py` can be imported from root directory

## Phase 2: Foundational

- [ ] T003 Create `backend/api.py` with basic FastAPI setup and CORS configuration
- [ ] T004 Define Pydantic models for `QueryRequest` and `QueryResponse` in `backend/api.py`

## Phase 3: User Story 1 - Backend API Access [US1]

**Goal**: Expose a functional endpoint that returns agent responses.
**Independent Test**: `curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"query": "test"}'`

- [ ] T005 [P] [US1] Implement `POST /chat` endpoint in `backend/api.py` using `Runner.run` and `rag_agent`
- [ ] T006 [US1] Implement input validation for empty queries in `POST /chat` in `backend/api.py`
- [ ] T007 [P] [US1] Create `backend/test_api.py` with `httpx` tests for success and failure cases

## Phase 4: User Story 2 - Frontend Chat Interface [US2]

**Goal**: Display a chat widget that interacts with the backend.
**Independent Test**: Use browser to send a message via UI and see response.

- [ ] T008 [P] [US2] Create `src/components/ChatWidget.tsx` with basic styles and state management
- [ ] T009 [US2] Implement API call logic in `src/components/ChatWidget.tsx` to fetch from `http://localhost:8000/chat`
- [ ] T010 [US2] Create `src/theme/Root.tsx` to wrap the Docusaurus app with the `ChatWidget` component
- [ ] T011 [US2] Add loading and error states to `src/components/ChatWidget.tsx`

## Phase 5: Polish & Cross-Cutting

- [ ] T012 Add markdown rendering to agent responses in `src/components/ChatWidget.tsx`
- [ ] T013 Update `README.md` with instructions on how to start both backend and frontend for integration

## Dependencies

- US1 must be completed (or mocked) to fully test US2.
- Foundational tasks (T003-T004) are required for US1.
