---
id: 002
title: Integrate RAG API Plan
stage: plan
date: 2025-12-27
surface: agent
model: gemini-2.0-flash-exp
feature: 004-integrate-rag-api
branch: 004-integrate-rag-api
user: user
command: /sp.plan
labels: ["plan", "design", "fastapi", "docusaurus"]
links:
  spec: specs/004-integrate-rag-api/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/004-integrate-rag-api/plan.md
 - specs/004-integrate-rag-api/research.md
 - specs/004-integrate-rag-api/data-model.md
 - specs/004-integrate-rag-api/contracts/api.yaml
 - specs/004-integrate-rag-api/quickstart.md
tests:
  null
---

## Prompt

Spec-4: Frontend-Backend Integration with FastAPI

Confirm existing chatbot UI in book_frontend/ (Docusaurus) is used as-is

Build chatbot UI to display across the entire book frontend

Create api.py at project root and set up FastAPI server

Expose a query endpoint that calls the agent from agent.py

Return agent responses to the frontend via JSON

## Response snapshot

Created implementation plan.
Decisions:
1. Use `src/theme/Root.tsx` to inject global Chat Widget (Swizzling).
2. Create `backend/api.py` for FastAPI server (not root, for cleanliness).
3. Reuse `agent.py` logic by importing `rag_agent`.
4. Create new `ChatWidget` component as none was found in `src/components`.

## Outcome

- ✅ Impact: Plan creates a bridge between existing Agent and Frontend.
- 🧪 Tests: Will add API tests and manual UI verification.
- 📁 Files: Plan artifacts generated.
- 🔁 Next prompts: /sp.tasks
- 🧠 Reflection: "book_frontend/" directory not found; assumed root is the frontend.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
