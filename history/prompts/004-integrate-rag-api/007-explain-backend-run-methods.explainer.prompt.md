---
id: 007
title: Explain Backend Run Methods
stage: explainer
date: 2025-12-27
surface: agent
model: gemini-2.0-flash-exp
feature: 004-integrate-rag-api
branch: 004-integrate-rag-api
user: user
command: explain backend run methods
labels: ["backend", "documentation", "fastapi"]
links:
  spec: specs/004-integrate-rag-api/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - backend/README.md
tests: []
---

## Prompt

yes backend is running but give me how to run backend my self i need many ways to run bakcend

## Response snapshot

Provided 4 methods to run the backend:
1.  **Via `uv` (Recommended)**: `uv run uvicorn api:app --reload`
2.  **Via `python` (Module)**: `python -m uvicorn api:app`
3.  **Direct Activation**: `.venv\Scripts\activate` then `uvicorn`
4.  **NPM Script (Proposed)**: Adding `"backend": "cd backend && uv run uvicorn api:app"` to `package.json`.

## Outcome

- ✅ Impact: User informed of multiple execution strategies.
- 🧪 Tests: N/A
- 📁 Files: None changed (information only).
- 🔁 Next prompts: N/A
- 🧠 Reflection: Clear documentation of run commands is essential for developer experience (DX).
