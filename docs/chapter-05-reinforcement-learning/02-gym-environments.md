---
title: Gymnasium Environments
sidebar_label: 2. Gym Environments
description: Simulating physics with OpenAI Gym / Farama Gymnasium.
---

# Gymnasium Environments

## Learning Objectives
- What is Gymnasium?
- Observation Space vs Action Space.
- Running a random agent.

## Setup
Gymnasium provides standard API for environments (CartPole, LunarLander, MuJoCo).

## Hands-on Exercise

### Random Walker
**Prerequisite**: `pip install gymnasium`

**Code**:
```python
import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset()

for _ in range(100):
    action = env.action_space.sample()  # Random action
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()
```

**Task**:
- Run the code.
- Observe the pole falling over immediately. Random actions don't work! We need to learn.
