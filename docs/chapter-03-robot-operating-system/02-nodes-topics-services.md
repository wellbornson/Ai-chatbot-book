---
title: Nodes, Topics, Services
sidebar_label: 2. Core Concepts
description: Deep dive into ROS 2 communication patterns.
---

# Nodes, Topics, and Services

## Learning Objectives
- Master Pub/Sub (Topics).
- Master Request/Response (Services).
- When to use which?

## 1. Topics (Publish/Subscribe)
Used for streaming data (sensor data, motor state).
- **One-to-Many**: One node publishes, many can subscribe.
- **Asynchronous**: Fire and forget.

## 2. Services (Client/Server)
Used for immediate tasks (e.g., "Reset Odometry", "Take Picture").
- **One-to-One**: Client requests, Server responds.
- **Synchronous**: Blocks until done.

## Hands-on Exercise

### CLI Tools
1. Start the simulation from the previous lesson (`talker` and `listener`).
2. List all active topics:
   ```bash
   ros2 topic list
   ```
3. Inspect the data stream:
   ```bash
   ros2 topic echo /chatter
   ```

**Task**:
- What is the message type of `/chatter`? Use `ros2 topic info /chatter`.
