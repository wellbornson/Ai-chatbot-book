# Tasks: Add Robotics Course Chapters

**Feature**: `005-add-course-chapters`
**Plan**: [plan.md](./plan.md)

## Implementation Strategy

We will proceed chapter by chapter, restructuring existing directories where necessary and generating the required lesson content. Finally, we will validate the build and ingestion.

## Phase 1: Setup & Restructuring

- [ ] T001 Rename `docs/chapter-02-sensors-and-perception` to `docs/chapter-02-actuators-and-control`
- [ ] T002 Rename `docs/chapter-03-actuators-and-control` to `docs/chapter-03-robot-operating-system`
- [ ] T003 Rename `docs/chapter-04-kinematics-and-dynamics` to `docs/chapter-04-computer-vision`
- [ ] T004 Rename `docs/chapter-05-control-systems` to `docs/chapter-05-reinforcement-learning`
- [ ] T005 Rename `docs/chapter-06-motion-planning` to `docs/chapter-06-edge-deployment`
- [ ] T006 Update `_category_.json` in each new folder to reflect the new titles (Actuators, ROS 2, Vision, RL, Edge)

## Phase 3: Chapter 2 - Actuators & Motor Control [US1]

**Goal**: Deliver lessons on controlling robot movement.
**Independent Test**: Build site and verify Ch 2 appears with 3 lessons.

- [ ] T007 [US1] Create `docs/chapter-02-actuators-and-control/01-introduction-to-actuators.md` with Hands-on Exercise
- [ ] T008 [US1] Create `docs/chapter-02-actuators-and-control/02-electric-motors.md` with Hands-on Exercise
- [ ] T009 [US1] Create `docs/chapter-02-actuators-and-control/03-motor-control-loops.md` with Hands-on Exercise

## Phase 4: Chapter 3 - ROS 2 Integration [US2]

**Goal**: Deliver lessons on Robot Operating System 2.

- [ ] T010 [US2] Create `docs/chapter-03-robot-operating-system/01-ros2-basics.md` with Hands-on Exercise
- [ ] T011 [US2] Create `docs/chapter-03-robot-operating-system/02-nodes-topics-services.md` with Hands-on Exercise
- [ ] T012 [US2] Create `docs/chapter-03-robot-operating-system/03-creating-packages.md` with Hands-on Exercise

## Phase 5: Chapter 4 - Computer Vision [US3]

**Goal**: Deliver lessons on robot perception.

- [ ] T013 [US3] Create `docs/chapter-04-computer-vision/01-camera-models.md` with Hands-on Exercise
- [ ] T014 [US3] Create `docs/chapter-04-computer-vision/02-opencv-basics.md` with Hands-on Exercise
- [ ] T015 [US3] Create `docs/chapter-04-computer-vision/03-object-detection-yolo.md` with Hands-on Exercise

## Phase 6: Chapter 5 - Reinforcement Learning [US4]

**Goal**: Deliver lessons on training agents.

- [ ] T016 [US4] Create `docs/chapter-05-reinforcement-learning/01-rl-fundamentals.md` with Hands-on Exercise
- [ ] T017 [US4] Create `docs/chapter-05-reinforcement-learning/02-gym-environments.md` with Hands-on Exercise
- [ ] T018 [US4] Create `docs/chapter-05-reinforcement-learning/03-training-ppo-agent.md` with Hands-on Exercise

## Phase 7: Chapter 6 - Edge Deployment [US5]

**Goal**: Deliver lessons on deploying to hardware.

- [ ] T019 [US5] Create `docs/chapter-06-edge-deployment/01-edge-hardware-overview.md` with Hands-on Exercise
- [ ] T020 [US5] Create `docs/chapter-06-edge-deployment/02-optimizing-models-onnx-tensorrt.md` with Hands-on Exercise
- [ ] T021 [US5] Create `docs/chapter-06-edge-deployment/03-deployment-pipeline.md` with Hands-on Exercise

## Phase 8: Final Polish & Ingestion

- [ ] T022 Run `npm run build` to verify all MDX content compiles
- [ ] T023 Run `/backend/main.py` (via python) to ingest new chapters into RAG index

## Dependencies

- Folder restructuring (Phase 1) MUST happen before file creation.
