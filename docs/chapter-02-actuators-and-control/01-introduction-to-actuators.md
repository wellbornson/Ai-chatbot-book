---
title: Introduction to Actuators
sidebar_label: 1. Actuator Basics
description: Understanding how robots move using various types of actuators.
---

# Introduction to Actuators

## Learning Objectives
- Understand what an actuator is.
- Differentiate between electric, hydraulic, and pneumatic actuators.
- Identify the role of actuators in a humanoid robot.

## What is an Actuator?
An actuator is a component of a machine that is responsible for moving and controlling a mechanism or system. It takes an energy source (electric current, hydraulic fluid pressure, or pneumatic pressure) and converts it into mechanical motion.

In simple terms, if sensors are the "eyes and ears" of a robot, actuators are its "muscles".

## Types of Actuators

### 1. Electric Actuators
The most common type in modern humanoid robots (like Tesla Optimus, Figure 01).
- **Pros**: Precise, clean, quiet, easy to control via software.
- **Cons**: Can overheat, lower power-to-weight ratio than hydraulics.

### 2. Hydraulic Actuators
Used in heavy-lifting robots (e.g., early Boston Dynamics Atlas).
- **Pros**: Extremely high force density, robust.
- **Cons**: Leaky, noisy, complex maintenance.

### 3. Pneumatic Actuators
Uses compressed air. Common in soft robotics.
- **Pros**: Compliant (soft), lightweight.
- **Cons**: "Spongy" control, requires air compressor.

## Hands-on Exercise

### Simulation: Controlling a Virtual Joint
In this exercise, we will conceptualize sending a command to an actuator.

**Scenario**: You have a robot arm with one elbow joint powered by a DC motor. You want to move it from 0 degrees to 90 degrees.

**Code Concept (Python-like pseudo-code)**:
```python
class Motor:
    def __init__(self):
        self.angle = 0

    def set_target(self, target_angle):
        print(f"Moving motor from {self.angle} to {target_angle}...")
        self.angle = target_angle

elbow_motor = Motor()
elbow_motor.set_target(90)
```

**Task**:
1. Imagine the motor cannot move instantly.
2. How would you modify the code to move the motor in small steps (1 degree at a time)?
