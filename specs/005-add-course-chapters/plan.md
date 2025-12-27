# Implementation Plan - Add Robotics Course Chapters

**Feature**: `005-add-course-chapters`
**Status**: Draft

## Technical Context

**Stack**:
- **Framework**: Docusaurus (Markdown/MDX).
- **Structure**: `docs/` folder with subdirectories per chapter.
- **Metadata**: `_category_.json` for sidebar, Frontmatter for pages.
- **Ingestion**: `backend/main.py` (Python) scans `docs/` to build RAG index.

**Current State**:
- `docs/` already has folders for Chapters 1-10 (from template?).
- `docs/chapter-02...` exists but only has `_category_.json`.
- Need to populate Chapters 2-6 with actual content files.

**Constraints**:
- Must match existing naming convention `chapter-XX-<topic>`.
- Must include "Hands-on Exercise" section.
- Must be valid MDX.

## Constitution Check

| Principle | Compliance Check |
|-----------|------------------|
| **Library-First** | Content is modular (chapters). |
| **CLI Interface** | N/A (Content only). |
| **Test-First** | Success criteria includes build check and ingestion check. |
| **Simplicity** | Using standard Docusaurus file structure. |

## Phase 0: Outline & Research

### Unknowns & Riskiest Assumptions
1.  **Existing Folders**: `ls docs` showed existing folders for Chapters 2-10.
    *   *Resolution*: I should **use the existing folders** instead of creating new ones if the names match, OR rename them to match the spec if they are different.
    *   *Current Names*:
        - Ch 2: `chapter-02-sensors-and-perception` (Spec asks for Actuators - Wait, Spec says Ch 2 is Actuators, but existing folder is Sensors. I will follow the SPEC topics. Existing folders might need renaming or I will just overwrite/use them).
        - *Correction*: Spec says "Chapter 2: Actuators". Existing Ch 2 is "Sensors". Existing Ch 3 is "Actuators".
        - *Decision*: I will **follow the User Spec** for topics. If folder names conflict, I will rename/repurpose the existing folders to match the requested topics to ensure the course flows as requested.
        - *Actually*: User Spec Ch 2 = Actuators. Existing Ch 3 = Actuators.
        - *Plan*: I will rename/re-structure to match the **Spec** exactly.
            - `docs/chapter-02-actuators` (was sensors)
            - `docs/chapter-03-ros2` (was actuators)
            - `docs/chapter-04-computer-vision` (was kinematics)
            - `docs/chapter-05-reinforcement-learning` (was control)
            - `docs/chapter-06-edge-deployment` (was motion planning)

### Research Tasks
- [x] Check existing `docs/` structure (Done).
- [ ] Verify `_category_.json` format in existing folders (Done - standard Docusaurus).

## Phase 1: Design & Contracts

### Data Model
**File Structure**:
- `docs/chapter-02-actuators-and-control/`
  - `_category_.json`
  - `01-introduction.md`
  - `02-types-of-actuators.md`
  - `03-motor-control-loops.md`
- ... (repeat for Ch 3-6)

### Components
- **Markdown Files**: 15 total (3 per chapter).
- **Assets**: Images (optional, placeholders if needed).

## Phase 2: Implementation Breakdown

### Tasks
1.  **Restructure Directories**: Rename/Create folders for Ch 2-6 to match Spec topics.
2.  **Generate Chapter 2**: Actuators (3 lessons).
3.  **Generate Chapter 3**: ROS 2 (3 lessons).
4.  **Generate Chapter 4**: Computer Vision (3 lessons).
5.  **Generate Chapter 5**: RL (3 lessons).
6.  **Generate Chapter 6**: Edge Deployment (3 lessons).
7.  **Verify**: Run build and ingestion.

## Security & Privacy
- No code execution in docs (static site).
- No sensitive data.