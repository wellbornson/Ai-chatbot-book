---
id: 011
title: Style AI Hero Image as HUD
stage: green
date: 2025-12-27
surface: agent
model: gemini-2.0-flash-exp
feature: 004-integrate-rag-api
branch: 004-integrate-rag-api
user: user
command: style AI logo like teacher greeting HUD
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

wow great AI main logo also change like ameen alam text left side same as same create AI logo

## Response snapshot

Applied the "Advanced HUD" styling to the central AI Hero Image.
1.  **React Structure (`src/pages/index.tsx`)**: Wrapped the creator info and hero image in a new `ai-hero-hud` container.
    -   Added matching `tech-corner` elements.
    -   Added a system status header (`SYSTEM: ONLINE`, `NEURAL_CORE_V2`).
    -   Added a `hologram-overlay` over the image for a TV-scan effect.
2.  **CSS Styling (`src/css/custom.css`)**:
    -   Created `.ai-hero-hud` with the same `clip-path` (cut corners) and metallic borders as the teacher greeting.
    -   Added a "hologram" scanline texture overlaying the image.
    -   Ensured the container centers properly on the page.

## Outcome

- ✅ Impact: The main visual element now matches the high-tech, military/cyberpunk aesthetic of the side greeting.
- 🧪 Tests: Visual verification required.
- 📁 Files: Modified `src/pages/index.tsx` and `src/css/custom.css`.
- 🔁 Next prompts: N/A
- 🧠 Reflection: Consistent styling across UI elements (Teacher Greeting + Hero Image) strengthens the theme significantly.
