---
id: 001
title: Add Course Chapters Spec
stage: spec
date: 2025-12-27
surface: agent
model: gemini-2.0-flash-exp
feature: 005-add-course-chapters
branch: 005-add-course-chapters
user: user
command: /sp.specify
labels: ["spec", "content", "docusaurus"]
links:
  spec: specs/005-add-course-chapters/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/005-add-course-chapters/spec.md
 - specs/005-add-course-chapters/checklists/requirements.md
tests:
  null
---

## Prompt

Build 5 additional chapters for the Physical AI & Humanoid Robotics Course. Requirements: Structure: Create Chapters 2 through 6. Each chapter must have exactly 3 lessons. Topics to Cover: > - Chapter 2: Actuators and Motor Control. Chapter 3: Robot Operating System (ROS 2) Integration. Chapter 4: Computer Vision for Humanoids. Chapter 5: Reinforcement Learning in Physical Environments. Chapter 6: Deploying AI Models to Edge Hardware (Jetson/Raspberry Pi). Format: Generate content in Docusaurus-compatible Markdown (.md). Include a "Hands-on Exercise" section for every lesson. Integration: Ensure all new content follows the metadata format required for the Spec-1 Ingestion Pipeline. Instruction: After generating the text, provide a checklist for adding these files to the docs/ folder and re-running the /backend/main.py ingestion script.

## Response snapshot

Created feature branch 005-add-course-chapters and spec file defining requirements for 5 new chapters (15 lessons total) with hands-on exercises and metadata compliance.

## Outcome

- ✅ Impact: Defined scope for major content expansion.
- 🧪 Tests: N/A
- 📁 Files: Spec and checklist created.
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: Script argument passing issue persisted but manual recovery successful.

## Evaluation notes (flywheel)

- Failure modes observed: PowerShell script parameter binding error.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
