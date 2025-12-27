# Implementation Plan - Integrate RAG API

**Feature**: `004-integrate-rag-api`
**Status**: Draft

## Technical Context

**Stack**:
- **Frontend**: Docusaurus (React/TypeScript).
- **Backend**: Python 3.11+, FastAPI.
- **Agent**: `backend/agent.py` (OpenAI Agents SDK).
- **Communication**: REST API (JSON).

**Architecture**:
- **Backend Service**: `backend/api.py` runs a FastAPI server.
- **Frontend Client**: React component (`ChatWidget`) injected into the Docusaurus app via `src/theme/Root.tsx`.
- **Data Flow**: User -> Frontend -> API -> Agent -> Logic -> Agent -> API -> Frontend.

**Constraints**:
- Backend must invoke `rag_agent` from `backend/agent.py`.
- Frontend must be visible globally (all pages).
- Local development environment.

## Constitution Check

| Principle | Compliance Check |
|-----------|------------------|
| **Library-First** | `api.py` acts as the interface library for the agent. |
| **CLI Interface** | `agent.py` already has CLI; API extends this to HTTP. |
| **Test-First** | Will write tests for API endpoints (`test_api.py`) and Frontend component (React tests if set up, otherwise manual). |
| **Simplicity** | Minimal API surface (single endpoint). Direct integration. |

## Phase 0: Outline & Research

### Unknowns & Riskiest Assumptions
1.  **Agent Async**: `agent.py` uses `asyncio.run` in CLI commands. We need to reuse the `async` function logic without creating a new event loop, as FastAPI manages its own.
    *   *Resolution*: Import `rag_agent` and `Runner` and call `await Runner.run(...)` directly in the FastAPI route handler.
2.  **Docusaurus Global Component**: Best way to inject ChatWidget?
    *   *Resolution*: Use `src/theme/Root.tsx` to wrap the app.

### Research Tasks
- [x] Confirm `backend/agent.py` structure (already read).
- [ ] Verify `src/theme/Root.tsx` is supported in current Docusaurus version (standard feature).

## Phase 1: Design & Contracts

### Data Model
**Entities**:
- `QueryRequest`: `{ "query": string, "thread_id": string? }`
- `QueryResponse`: `{ "response": string, "thread_id": string }`

### API Contracts
- `POST /chat`:
    - Request: `QueryRequest`
    - Response: `QueryResponse`
    - Errors: 400 (Validation), 500 (Agent error).

### Components
1.  `backend/api.py`: FastAPI app entrypoint.
2.  `src/components/ChatWidget.tsx`: The UI component.
3.  `src/theme/Root.tsx`: Global wrapper.

## Phase 2: Implementation Breakdown

### Tasks
1.  Create `backend/api.py` with FastAPI setup and `rag_agent` import.
2.  Create `backend/test_api.py` to verify endpoint.
3.  Create `src/components/ChatWidget.tsx` (UI + Logic).
4.  Create `src/theme/Root.tsx` to inject widget.
5.  Update `package.json` or `README` with run instructions.

## Security & Privacy
- CORS enabled for local development (restrict to frontend origin in prod).
- No sensitive data logged.