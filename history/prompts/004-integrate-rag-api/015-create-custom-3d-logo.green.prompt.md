---
id: 015
title: Create Custom 3D Animated Logo
stage: green
date: 2025-12-27
surface: agent
model: gemini-2.0-flash-exp
feature: 004-integrate-rag-api
branch: 004-integrate-rag-api
user: user
command: create fully custom 3D movable AI logo
labels: ["frontend", "css", "animation", "3d"]
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

no no this is not good i want to remove these textes "zahid mobile #03174446660" and exchange to AI logo and should be big logo and fully movable and fully 3D custumise

## Response snapshot

1.  **Removed Text**: Completely removed the "ZAHID MOBILE" text section from `src/pages/index.tsx`.
2.  **Custom 3D Logo**: Replaced the image with a **Pure CSS 3D Cube** structure (`.scene-3d`, `.cube-3d`).
    *   **Movable**: It spins endlessly on X and Y axes (`spinCube` animation).
    *   **Custom**: Built from scratch using CSS `transform-style: preserve-3d`.
    *   **Big**: 200x200px cube (appearing larger due to rotation).
    *   **AI Branding**: The text "AI" is embedded on the cube faces.
    *   **Core**: Added a glowing pulsing core inside the transparent cube for a "reactor" look.

## Outcome

- ✅ Impact: A truly "fully 3D and customised" animated logo that replaces the static image and text.
- 🧪 Tests: Visual verification required.
- 📁 Files: Modified `src/pages/index.tsx` and `src/css/custom.css`.
- 🔁 Next prompts: N/A
- 🧠 Reflection: CSS 3D is a lightweight way to achieve "fully movable 3D" without heavy libraries like Three.js.
