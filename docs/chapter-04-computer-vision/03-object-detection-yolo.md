---
title: Object Detection (YOLO)
sidebar_label: 3. YOLO Detection
description: Using Deep Learning to find objects.
---

# Object Detection (YOLO)

## Learning Objectives
- Image Classification vs. Object Detection.
- How YOLO (You Only Look Once) works.
- Running YOLOv8 on a robot.

## Why YOLO?
Traditional CV (like color filtering) fails when lighting changes. Neural Networks (YOLO) learn features and are robust.

## Hands-on Exercise

### Run YOLOv8
**Prerequisite**: `pip install ultralytics`

**Code**:
```python
from ultralytics import YOLO
import cv2

# Load model
model = YOLO('yolov8n.pt')  # Nano model (fastest)

# Predict on webcam
results = model(source=0, show=True, conf=0.5)
```

**Task**:
- Run the script.
- Show the camera your phone or a bottle. Does it classify it correctly?
