---
title: Model Optimization
sidebar_label: 2. Optimization (ONNX/TensorRT)
description: Making models faster for small devices.
---

# Model Optimization

## Learning Objectives
- Quantization (FP32 -> INT8).
- Pruning.
- Exporting to ONNX and TensorRT.

## Why Optimize?
A heavy PyTorch model might run at 5 FPS on a Pi. Converting to ONNX/TensorRT can boost it to 30 FPS.

## Hands-on Exercise

### PyTorch to ONNX
**Code**:
```python
import torch
import torchvision.models as models

# Load standard model
model = models.resnet18(pretrained=True)
model.eval()

# Dummy input
dummy_input = torch.randn(1, 3, 224, 224)

# Export
torch.onnx.export(model, dummy_input, "resnet18.onnx")
print("Exported to resnet18.onnx")
```

**Task**:
- Run the script.
- Check the file size of the `.onnx` file compared to the PyTorch checkpoint.
