---
title: ROS 2 Basics
sidebar_label: 1. ROS 2 Basics
description: Getting started with the Robot Operating System.
---

# ROS 2 Basics

## Learning Objectives
- What is ROS 2?
- Understanding Nodes and the Graph.
- Installing ROS 2 (Humble/Iron).

## What is ROS 2?
ROS (Robot Operating System) is not an OS like Windows or Linux. It is a **middleware**—a set of software libraries and tools that help you build robot applications. It handles communication between different parts of your robot (e.g., camera talking to the motor controller).

## Key Concept: The Graph
ROS 2 programs are made of **Nodes**.
- **Node**: A single process performing a specific task (e.g., "Read Camera", "Drive Motors").
- **Graph**: The network of connected Nodes.

## Hands-on Exercise

### Install Check & Hello World
Assuming you have a Linux environment or WSL setup:

1. **Install ROS 2** (Follow official docs for 'Humble').
2. **Run the demo**:
   Terminal 1 (Talker):
   ```bash
   ros2 run demo_nodes_cpp talker
   ```
   Terminal 2 (Listener):
   ```bash
   ros2 run demo_nodes_py listener
   ```

**Task**:
- Observe how Terminal 2 prints what Terminal 1 is sending.
- This is the essence of ROS: data passing between independent programs.
