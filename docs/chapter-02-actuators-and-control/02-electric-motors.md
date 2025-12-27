---
title: Electric Motors
sidebar_label: 2. Electric Motors
description: Deep dive into DC, BLDC, and Stepper motors for robotics.
---

# Electric Motors

## Learning Objectives
- Compare DC, BLDC, and Stepper motors.
- Understand Kv ratings and torque constants.
- Learn why Brushless DC (BLDC) motors are preferred for humanoids.

## Types of Electric Motors

| Motor Type | Description | Best For |
|------------|-------------|----------|
| **Brushed DC** | Simple, cheap, easy to drive. | Hobby projects, simple wheels. |
| **Stepper** | Moves in precise discrete steps. High holding torque. | 3D printers, precision arms. |
| **Brushless DC (BLDC)** | Efficient, high torque, reliable, requires complex driver (ESC). | Humanoid joints, drones, walking robots. |

## Why BLDC for Humanoids?
Humanoid robots need high torque to hold poses (like standing on one leg) and high efficiency to run on batteries. BLDC motors offer the best balance. They are often coupled with **gearboxes** (like planetary or harmonic drives) to multiply torque.

## Hands-on Exercise

### Choosing a Motor
**Scenario**: You are building a humanoid leg joint. You need to lift 5kg at a distance of 0.5m.

**Calculation**:
1. Calculate required Torque ($\tau$).
   - $\tau = \text{Force} \times \text{Distance}$
   - Force ($F$) = Mass ($m$) $\times$ Gravity ($g$) $\approx 5 \text{kg} \times 9.81 \text{m/s}^2 \approx 49 \text{N}$.
   - $\tau = 49 \text{N} \times 0.5 \text{m} = 24.5 \text{Nm}$.

**Task**:
- Look up a standard "AK80-9" actuator (common in robotics).
- Does it meet this torque requirement? (Hint: Peak torque is usually ~48Nm).
