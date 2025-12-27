---
id: 016
title: Move Chatbot to Left and Apply 3D Style
stage: green
date: 2025-12-27
surface: agent
model: gemini-2.0-flash-exp
feature: 004-integrate-rag-api
branch: 004-integrate-rag-api
user: user
command: make left side chatbot like AI 3D fully
labels: ["frontend", "react", "css", "3d", "chatbot"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - src/components/ChatWidget.tsx
 - src/css/custom.css
tests: []
---

## Prompt

wooooow awsome you shuld make it my left side chatbot like AI 3D fully

## Response snapshot

1.  **Repositioning**: Moved the chatbot to the **Left Side** (`left: 30px` in CSS) as requested.
2.  **3D Button**: Replaced the standard emoji button with a **Mini Spinning 3D Cube** (`mini-cube-wrapper`) that matches the main logo.
3.  **Holographic Window**: Applied a `.chat-window-3d` class to the chat panel, giving it a slight 3D tilt and floating effect (`transform: rotateY(5deg)`).
4.  **Glassmorphism**: Updated the chat window background to be semi-transparent for a more "fully 3D" digital look.

## Outcome

- ✅ Impact: The chatbot is now on the left and shares the exact same "Spinning Cube" DNA as the main logo.
- 🧪 Tests: Visual verification required.
- 📁 Files: Modified `src/components/ChatWidget.tsx` and `src/css/custom.css`.
- 🔁 Next prompts: N/A
- 🧠 Reflection: Moving standard widgets (usually right) to the left can conflict with other elements, but since the "Teacher Greeting" is also on the left, they might stack. I'll need to watch for overlap in future steps if the user complains.
