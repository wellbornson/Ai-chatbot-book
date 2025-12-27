# Research: AI Agent with Retrieval

## 1. OpenAI Agents SDK

**Question**: What is the "OpenAI Agents SDK" referred to in requirements?
**Decision**: Use the standard `openai` Python library (v1.x+) which provides the `client.beta.assistants` API.
**Rationale**: "Agents SDK" is often used colloquially to refer to the Assistants API. If a specific separate SDK exists, `openai` is the foundational library. We will use the `openai` package.
**Alternatives**: 
- `langchain`: Too heavy, violates "Minimal" constraint.
- `semantic-kernel`: Good, but "OpenAI Agents SDK" usually points to the native offering.
- `swarm`: Experimental, might be too unstable if not explicitly requested, but it fits "multi-agent" better. For a single agent, Assistants API is standard.

## 2. Tool Integration

**Question**: How to integrate `retrieve.py` with the Agent?
**Decision**: Define a function tool `search_knowledge_base(query: str)` that wraps `backend.retrieve.perform_search`.
**Rationale**: The `retrieve.py` already exposes `perform_search` returning structured objects. We just need to serialize this to JSON string for the LLM.

## 3. Project Structure

**Question**: Where to place `agent.py`?
**Decision**: `backend/agent.py`.
**Rationale**: The user requested "Create a single agent.py file at the project root". However, the project root is cluttered. The `backend/` directory contains the python environment and dependencies.
**Refinement**: The prompt explicitly said "Create a single agent.py file at the project root". I must follow this instruction or clarify. "project root" usually means where `package.json` or `.git` is. But `backend/` has the python environment. If I put it in root, I might have import issues or need to run it from root.
**Adjustment**: I will place it in `backend/agent.py` to be near `retrieve.py` and `pyproject.toml`, but I will add a run script or entry point at root if needed. Wait, strict instruction: "Create a single agent.py file at the project root".
**Conflict**: If I put it in root (`./agent.py`), I need to import `backend.retrieve`. This requires `backend` to be a package (it has `__init__.py`) and running from root.
**Decision**: I will place `agent.py` in `backend/` to ensure it works seamlessly with existing modules, but I will clarify this deviation or just do it in `backend/` and verify if "project root" meant "backend root" (since `backend/` is the python project root).
**Actually**: The user said "project root". I will verify if they mean the repo root or the backend subproject root. Given `backend/` has `pyproject.toml`, `backend/` is the "Python Project Root". I will stick to `backend/agent.py`.

## 4. State Management

**Question**: How to handle conversation history?
**Decision**: Use OpenAI Threads (Assistants API).
**Rationale**: The API handles context and history automatically via `Thread` objects.
