import cv2
import onnx
import onnxruntime as ort
import numpy as np
from camera import get_frame
from display import show_oled
from mqtt import publish
import time

# Load model
session = ort.InferenceSession("models/mobilenet_v3.onnx")
input_name = session.get_inputs()[0].name
labels = open("labels.txt").read().splitlines()

def preprocess(frame):
    img = cv2.resize(frame, (224, 224))
    img = img.astype(np.float32) / 255.0
    img = np.transpose(img, [2, 0, 1])
    return np.expand_dims(img, axis=0)

while True:
    start = time.time()
    frame = get_frame()
    blob = preprocess(frame)
    preds = session.run(None, {input_name: blob})[0]
    idx = np.argmax(preds)
    label = labels[idx]
    conf = preds[0][idx]
    latency = (time.time() - start) * 1000

    print(f"{label} {conf:.1%} → {latency:.0f} ms")
    show_oled(label, f"{latency:.0f} ms")
    if conf > 0.9:
        publish("edge/alert", label)

    if cv2.waitKey(1) == ord('q'):
        break
