---
id: 004
title: Fix MDX compilation error in edge hardware overview
stage: green
date: 2025-12-27
surface: agent
model: gemini-2.0-flash
feature: 005-add-course-chapters
branch: 005-add-course-chapters
user: wellbornsonAi
command: none
labels: ["mdx", "bugfix", "docusaurus"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - docs/chapter-06-edge-deployment/01-edge-hardware-overview.md
tests:
  - none
---

## Prompt

got this error Microsoft Windows [Version 10.0.19045.6466]
(c) Microsoft Corporation. All rights reserved.

C:\Users\wellbornsonAi\Desktop\old-vercel>npm start

> web-book@0.0.0 start
> docusaurus start

[INFO] Starting the development server...√ [WARNING] Something is already running on port 3000.

Would you like to run the app on another port instead? ... yes
[SUCCESS] Docusaurus website is running at: http://localhost:3001/

× Client
  Compiled with some errors in 7.98s

Error: MDX compilation failed for file "C:\Users\wellbornsonAi\Desktop\old-vercel\docs\chapter-06-edge-deployment\01-edge-hardware-overview.md"
Cause: Unexpected character `1` (U+0031) before name, expected a character that can start a name, such as a letter, `$`, or `_`
Details:
{
  "column": 68,
  "file": "",
  "message": "Unexpected character `1` (U+0031) before name, expected a character that can start a name, such as a letter, `$`, or `_`",
  "line": 23,
  "name": "23:68",
  "place": {
    "_bufferIndex": 67,
    "_index": 0,
    "line": 23,
    "column": 68,
    "offset": 649
  },
  "reason": "Unexpected character `1` (U+0031) before name, expected a character that can start a name, such as a letter, `$`, or `_`",
  "ruleId": "unexpected-character",
  "source": "micromark-extension-mdx-jsx",
  "url": "https://github.com/micromark/micromark-extension-mdx-jsx#unexpected-character-at-expected-expect"
}
client (webpack 5.103.0) compiled with 1 error
<w> [webpack.cache.PackFileCacheStrategy] Skipped not serializable cache item 'Compilation/modules|C:\Users\wellbornsonAi\Desktop\old-vercel\node_modules\@docusaurus\mdx-loader\lib\index.js??ruleSet[1].rules[8].use[0]!C:\Users\wellbornsonAi\Desktop\old-vercel\docs\chapter-06-edge-deployment\01-edge-hardware-overview.md': No serializer registered for VFileMessage
<w> while serializing webpack/lib/cache/PackFileCacheStrategy.PackContentItems -> webpack/lib/NormalModule -> webpack/lib/ModuleBuildError -> Error -> VFileMessage

## Response snapshot

I identified that the MDX compilation error was caused by an unescaped `<` character followed immediately by a digit (`<10ms`) on line 23 of `docs/chapter-06-edge-deployment/01-edge-hardware-overview.md`. MDX interpreted this as an invalid JSX tag. I fixed the issue by escaping the `<` character (`\<10ms`).

## Outcome

- √ Impact: Fixed build error preventing Docusaurus from starting.
- ✨ Tests: Manual inspection confirmed the problematic character was at the reported line and column.
- 💿 Files: Modified `docs/chapter-06-edge-deployment/01-edge-hardware-overview.md`.
- ↩️ Next prompts: none
- 𞨋 Reflection: MDX is very strict about `<` characters. Always escape them when used as "less than" symbols in text.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
