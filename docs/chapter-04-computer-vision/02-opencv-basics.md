---
title: OpenCV Basics
sidebar_label: 2. OpenCV Basics
description: Image processing with Python.
---

# OpenCV Basics

## Learning Objectives
- Reading and showing images.
- Color spaces (RGB vs HSV).
- Basic filtering (Blur, Canny Edge).

## What is OpenCV?
OpenCV (Open Source Computer Vision Library) is the standard library for image processing.

## Hands-on Exercise

### Detect a Red Ball
**Scenario**: Your robot needs to follow a red ball.

**Code**:
```python
import cv2
import numpy as np

# Load image
img = cv2.imread('ball.jpg')

# Convert to HSV (Hue, Saturation, Value) - easier to filter color
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define red range
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

# Mask
mask = cv2.inRange(hsv, lower_red, upper_red)

# Show
cv2.imshow('Mask', mask)
cv2.waitKey(0)
```

**Task**:
- Run this script with any image containing a red object.
- Adjust `lower_red` and `upper_red` if it misses some red parts.
