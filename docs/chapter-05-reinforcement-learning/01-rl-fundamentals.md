---
title: RL Fundamentals
sidebar_label: 1. RL Basics
description: Agents, Environments, and Rewards.
---

# Reinforcement Learning Fundamentals

## Learning Objectives
- Define Agent, Environment, State, Action, Reward.
- Exploration vs Exploitation.

## The Loop
1. Agent sees **State** ($S_t$).
2. Agent takes **Action** ($A_t$).
3. Environment returns new **State** ($S_{t+1}$) and **Reward** ($R_{t+1}$).
4. Goal: Maximize cumulative reward.

## Hands-on Exercise

### Design a Reward Function
**Scenario**: You want a humanoid to walk forward.

**Proposed Rewards**:
1. $+1$ for every meter moved forward.
2. $-100$ if it falls over.
3. $-0.1$ for every unit of energy used (efficiency).

**Task**:
- What happens if you remove the "falls over" penalty? (The robot might just dive forward to gain distance quickly before crashing).
- Why is Reward Engineering difficult?
