---
title: Motor Control Loops
sidebar_label: 3. Control Loops
description: Implementing PID control for precise motor positioning.
---

# Motor Control Loops

## Learning Objectives
- Define the Feedback Loop.
- Understand P, I, and D terms.
- Tune a simple PD controller.

## The Feedback Loop
To control a robot joint, we don't just "tell" it where to go; we monitor where it *is* and correct the error.

1. **Target**: Desired angle (e.g., 90°).
2. **Actual**: Current angle measured by Encoder (e.g., 88°).
3. **Error**: Target - Actual (2°).
4. **Output**: Command sent to motor to reduce error.

## PID Controller
The most common control algorithm:
- **P (Proportional)**: Push harder if the error is large.
- **I (Integral)**: Push harder if the error persists over time (fixes steady-state error).
- **D (Derivative)**: Push *less* if we are closing the gap too fast (dampening).

Equation:
$$u(t) = K_p e(t) + K_i \int e(t) dt + K_d \frac{de(t)}{dt}$$

## Hands-on Exercise

### Tuning a P-Controller
Imagine a function `control(error)` that returns voltage.

```python
Kp = 0.5  # Proportional Gain

def get_motor_command(target, actual):
    error = target - actual
    command = Kp * error
    return command

# Test
print(get_motor_command(90, 80)) # Error 10 -> Command 5.0
print(get_motor_command(90, 89)) # Error 1 -> Command 0.5
```

**Task**:
1. What happens if `Kp` is too high? (The robot might shake/oscillate).
2. What happens if `Kp` is too low? (The robot moves too slowly).
