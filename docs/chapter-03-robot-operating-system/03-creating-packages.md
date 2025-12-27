---
title: Creating Packages
sidebar_label: 3. Your First Package
description: Writing custom ROS 2 code in Python.
---

# Creating Packages

## Learning Objectives
- Workspace structure (`src/`).
- `colcon build`.
- Writing a simple Python publisher.

## The Workspace
ROS 2 development happens in a workspace (usually `~/ros2_ws`).
Structure:
```
~/ros2_ws/
    src/
    build/
    install/
    log/
```

## Hands-on Exercise

### Create and Build
1. Go to your workspace `src` folder:
   ```bash
   cd ~/ros2_ws/src
   ```
2. Create a Python package:
   ```bash
   ros2 pkg create --build-type ament_python my_robot_controller
   ```
3. Build it:
   ```bash
   cd ~/ros2_ws
   colcon build
   ```
4. Source the setup file:
   ```bash
   source install/setup.bash
   ```

**Task**:
- Create a file `my_first_node.py` inside the package.
- Make it print "Hello from my robot!" every second.
