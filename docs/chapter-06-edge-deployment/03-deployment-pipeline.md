---
title: Deployment Pipeline
sidebar_label: 3. Deployment CI/CD
description: Automating updates to your robot fleet.
---

# Deployment Pipeline

## Learning Objectives
- Containerization (Docker).
- Over-the-Air (OTA) updates.
- Monitoring.

## Docker on Robots
"It worked on my laptop" is the enemy of robotics. Docker ensures the environment (ROS version, Python libs) is identical on the robot.

## Hands-on Exercise

### Write a Dockerfile
**Task**: Create a `Dockerfile` for your ROS 2 node.

```dockerfile
FROM ros:humble-ros-base

# Install dependencies
RUN apt-get update && apt-get install -y python3-pip

# Copy code
COPY my_robot_controller /app/my_robot_controller

# Set entrypoint
CMD ["python3", "/app/my_robot_controller/my_first_node.py"]
```

**Question**:
- Why do we base it on `ros:humble-ros-base`? (It comes with ROS pre-installed).
