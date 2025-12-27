---
id: 015
title: rag-agent-official-sdk-refactor
stage: refactor
date: 2025-12-26
surface: agent
model: gemini-2.0-flash-exp
feature: rag-agent
branch: 003-rag-agent
user: wellbornsonAi
command: "agent.py file is working fine... use OpenAI Agents SDK instead of OpenAI Chat Completions/openai_client in agent.py file"
labels: ["refactor", "rag-agent", "openai-agents", "sdk"]
links:
  spec: specs/003-rag-agent/spec.md
  plan: specs/003-rag-agent/plan.md
  tasks: specs/003-rag-agent/tasks.md
  ticket: null
  adr: null
  pr: null
files:
 - backend/agent.py
 - backend/tests/test_agent.py
 - backend/pyproject.toml
tests:
 - backend/tests/test_agent.py (PASS)
---

## Prompt

agent.py file is working fine correctly and everything is okay but you have contenxt7 mcp server in this server you have official OpenAI Agents Python docs now you can use OpenAI Agents SDK instead OpenAI Chat Completions/openai_client in agent.py file

## Response snapshot

Refactored `backend/agent.py` to use the official `openai-agents` SDK. Replaced `swarm` (temporary choice) with the production-ready `Agent`, `Runner`, and `SQLiteSession` from `openai-agents`. Improved session management and tool definition using `@function_tool`.

## Outcome

- ✅ Impact: Modernized agent architecture using official OpenAI framework.
- 🧪 Tests: 3 unit tests passed (Config, Logic, Runner Flow).
- 📁 Files: agent.py, test_agent.py, pyproject.toml.
- 🔁 Next prompts: None.
- 🧠 Reflection: The official SDK (`openai-agents`) provides better abstraction for sessions and orchestration than manual Assistant API or Swarm.

## Evaluation notes (flywheel)

- Failure modes observed: `TypeError` on `FunctionTool` call in tests, `NameError` on `name_override`.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
