# Research: Integrate RAG API

**Status**: Complete
**Date**: 2025-12-27

## Decisions

### 1. Docusaurus Integration Strategy
**Decision**: Use `src/theme/Root.tsx`.
**Rationale**: This is the "Swizzling" independent way to render a component at the very top of the React tree, ensuring the Chat Widget persists across page navigations and is always visible.
**Alternatives**:
- `Layout` Swizzling: More fragile if Docusaurus theme changes.
- `docusaurus.config.ts` scripts: Can't easily render React components.

### 2. FastAPI Async Integration
**Decision**: Await `Runner.run` directly.
**Rationale**: FastAPI handles the event loop. `agent.py`'s `main()` functions use `asyncio.run()` which starts a *new* loop. We cannot use those `main` wrappers. We must import `rag_agent` and `Runner` and use the underlying async methods directly.
**Code Pattern**:
```python
@app.post("/chat")
async def chat_endpoint(request: QueryRequest):
    session = get_session(request.thread_id)
    result = await Runner.run(rag_agent, request.query, session=session)
    return {"response": result.final_output}
```

### 3. API Location
**Decision**: `backend/api.py`.
**Rationale**: Keeps python code isolated from Node.js frontend code. Cleaner project structure.

## Dependencies
- `fastapi`, `uvicorn`: For the server.
- `pydantic`: For validation.
- `lucide-react` (optional): For icons, or use standard SVGs to avoid deps. *Decision: Use SVGs or existing icons.*
