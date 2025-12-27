---
title: Edge Hardware Overview
sidebar_label: 1. Edge Hardware
description: Jetson Orin vs Raspberry Pi vs TPU.
---

# Edge Hardware Overview

## Learning Objectives
- Define "Edge Computing".
- Compare Hardware accelerators.
- Power constraints.

## The Contenders

| Device | AI Accelerator | Best For |
|--------|----------------|----------|
| **Raspberry Pi 5** | CPU / VideoCore (Weak for AI) | Low cost, simple logic. |
| **NVIDIA Jetson Orin Nano** | GPU (Ampere) | Running YOLO, ROS 2, serious robotics. |
| **Coral TPU** | ASIC | Specific TFLite models. |

## Why Edge?
A robot cannot rely on Cloud Wi-Fi for balancing. Latency must be \<10ms. Inference must happen locally.

## Hands-on Exercise

### Power Budget Calculation
**Scenario**: Your robot has a 12V 5000mAh battery (60Wh).
- Motors consume 50W.
- Jetson consumes 15W.
- Total Load: 65W.

**Task**:
- Calculate Runtime: Divide 60Wh by 65W. The result is roughly 0.92 hours, which is about 55 minutes.
- Is this enough for your mission?
