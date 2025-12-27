---
title: Training PPO Agent
sidebar_label: 3. Training PPO
description: Using Stable Baselines3 to learn policy.
---

# Training PPO Agent

## Learning Objectives
- What is PPO (Proximal Policy Optimization)?
- Training pipeline.
- Saving/Loading models.

## Why PPO?
It's the industry standard for robotics (used by OpenAI, Boston Dynamics). Stable and reliable compared to other algorithms (like DQN).

## Hands-on Exercise

### Train CartPole
**Prerequisite**: `pip install stable-baselines3`

**Code**:
```python
import gymnasium as gym
from stable_baselines3 import PPO

# Create env
env = gym.make("CartPole-v1")

# Create model
model = PPO("MlpPolicy", env, verbose=1)

# Train
print("Training...")
model.learn(total_timesteps=10000)

# Evaluate
print("Done! Testing...")
vec_env = model.get_env()
obs = vec_env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render("human")
```

**Task**:
- Run the training.
- Does the pole stay upright longer than the random agent?
