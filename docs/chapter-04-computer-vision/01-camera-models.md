---
title: Camera Models
sidebar_label: 1. Camera Models
description: Understanding Pinhole cameras and Intrinsic Matrices.
---

# Camera Models

## Learning Objectives
- The Pinhole Camera Model.
- Intrinsic vs. Extrinsic Parameters.
- Distortion.

## How Robots "See"
Robots don't see images; they see 2D arrays of numbers (pixels). To map a 3D world point $(X, Y, Z)$ to a 2D pixel $(u, v)$, we need math.

## The Pinhole Model
The simplest projection:
$$x = f \frac{X}{Z}$$
$$y = f \frac{Y}{Z}$$
where $f$ is the focal length.

## Hands-on Exercise

### Calibration Concept
You don't need code for this thought experiment.

**Scenario**: You have a robot camera. Objects look "curved" at the edges (fisheye effect).
**Task**:
1. Why does this happen? (Lens distortion).
2. Look up "Checkerboard Calibration". Why do roboticists wave a checkerboard in front of a robot? (To calculate the distortion matrix $D$ and un-warp the image).
