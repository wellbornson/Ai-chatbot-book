---
id: 010
title: Upgrade Teacher Greeting to Advanced HUD
stage: green
date: 2025-12-27
surface: agent
model: gemini-2.0-flash-exp
feature: 004-integrate-rag-api
branch: 004-integrate-rag-api
user: user
command: upgrade teacher greeting to advanced HUD
labels: ["frontend", "react", "css", "styling", "cyberpunk"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - src/pages/index.tsx
 - src/css/custom.css
tests: []
---

## Prompt

left side of you wrote sir ameen alam and sir zia khan these i want to more durable more effecincy more relible more advance its change it

## Response snapshot

Upgraded the teacher greeting to a "Cyberpunk HUD" style.
1.  **React Structure (`src/pages/index.tsx`)**: Replaced the simple greeting with a complex HUD panel containing:
    -   Corner bracket elements (`tech-corner`).
    -   System status header (`SYSTEM: SECURE`, `MENTOR_NODE_01`).
    -   Labeled mentor blocks (e.g., "LEAD INSTRUCTOR").
    -   A dedicated message box with a "data stream" header.
2.  **CSS Styling (`src/css/custom.css`)**:
    -   **Durability**: Added a "Clip-path" cut corner design and solid metallic borders.
    -   **Efficiency/Advanced**: Added a vertical "scan line" animation, blinking system indicators, and hover effects on mentor blocks.
    -   **Visuals**: Darker tech background with neon cyan/green accents for a "high-reliability" military/tech aesthetic.

## Outcome

- ✅ Impact: The greeting now looks like a piece of advanced technology or military HUD.
- 🧪 Tests: Visual verification required.
- 📁 Files: Modified `src/pages/index.tsx` and `src/css/custom.css`.
- 🔁 Next prompts: N/A
- 🧠 Reflection: The "Clip-path" polygon is a great way to make standard boxes look "advanced" without extra images.
