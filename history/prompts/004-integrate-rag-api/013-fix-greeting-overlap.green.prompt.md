---
id: 013
title: Fix Greeting Overlap and Remove Text
stage: green
date: 2025-12-27
surface: agent
model: gemini-2.0-flash-exp
feature: 004-integrate-rag-api
branch: 004-integrate-rag-api
user: user
command: fix greeting overlap and remove text
labels: ["frontend", "react", "styling", "layout"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - src/pages/index.tsx
tests: []
---

## Prompt

Physical AI & Humanoid Robotics Course " its line not clear shown because of left side sir ameen alam texted thats why i want to show these words clearly "Physical AI & Humanoid Robotics Course"  and i want to change this texted "● SYSTEM: SECURE
:: MENTOR_NODE_01 ::
LEAD INSTRUCTOR
SIR AMEEN ALAM
CHIEF VISIONARY
SIR ZIA KHAN
" these texted should be stay it but bottom of sir zia khan romove it or cut it.

## Response snapshot

1.  **Teacher Greeting**: Removed the "Incoming Transmission..." message box from `src/pages/index.tsx`, ending the widget after "SIR ZIA KHAN".
2.  **Main Title Visibility**: Added a backdrop and z-index to the `hero__title` ("Physical AI & Humanoid Robotics Course") to ensure it sits *above* any potential overlaps and is clearly legible with a text shadow and dark background blur.

## Outcome

- ✅ Impact: The teacher widget is more compact, and the main course title is now clearly visible regardless of screen size overlapping.
- 🧪 Tests: Visual verification required.
- 📁 Files: Modified `src/pages/index.tsx`.
- 🔁 Next prompts: N/A
- 🧠 Reflection: Using a semi-transparent background on the title text is a robust way to guarantee legibility against busy backgrounds or overlapping elements.
