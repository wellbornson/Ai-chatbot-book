---
id: 014
title: rag-agent-refactor-swarm
stage: refactor
date: 2025-12-26
surface: agent
model: gemini-2.0-flash-exp
feature: rag-agent
branch: 003-rag-agent
user: wellbornsonAi
command: "you have contenxt7 mcp server... use OpenAI Agents SDK instead OpenAI Chat Completions in agent.py file"
labels: ["refactor", "rag-agent", "swarm", "openai-agents-sdk"]
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
tests:
 - backend/tests/test_agent.py (PASS)
---

## Prompt

you have contenxt7 mcp server in this server you have official OpenAI Agents Python docs now you can use OpenAI Agents SDK instead OpenAI Chat Completions in agent.py file

## Response snapshot

Refactored `backend/agent.py` to use the `swarm` library (identified as "OpenAI Agents SDK"). Replaced manual Assistants API logic with `Swarm` client and `Agent` definition. Updated tests to match new architecture.

## Outcome

- ✅ Impact: Simplified agent code using Swarm framework.
- 🧪 Tests: 3 unit tests passed (Config, Tool Wrapper, Run Flow).
- 📁 Files: agent.py, test_agent.py, pyproject.toml (added swarm).
- 🔁 Next prompts: None.
- 🧠 Reflection: "OpenAI Agents SDK" terminology was ambiguous; identified `swarm` as the likely target. "context7" was not accessible, so relied on web search to confirm SDK details.

## Evaluation notes (flywheel)

- Failure modes observed: `AttributeError` on `Agent.tools` (should be `functions`), `OpenAIError` on `Swarm()` init in tests.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
