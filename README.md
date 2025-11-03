# Edge-AI Inference Node  
**ONNX + Raspberry Pi • GitHub-Ready • <150 ms latency**

**Before:** 1.8 sec on cloud  
**After:** **137 ms** → **92 % faster**  
**One Pi → 7.3 inferences/sec** on 640×480 images

Runs **any ONNX CNN** (MobileNet, EfficientNet-Lite, YOLO-Nano)  
Zero cloud. Zero fees. 100 % offline.

---

## Diagram: 137 ms Pipeline 

```mermaid
graph LR
    A[Camera 640×480] --> B[PiCamera2]
    B --> C[Pre-process\nResize + Normalize]
    C --> D[ONNX Runtime\nGPU/CPU]
    D --> E[Post-process\nNMS + Labels]
    E --> F[OLED Display\n+ MQTT Alert]
    style D fill:#FF5722,color:white
    style F fill:#4CAF50,color:white
