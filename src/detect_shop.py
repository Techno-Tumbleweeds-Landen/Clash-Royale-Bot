# src/run_model.py
import sys
import time
import os

import cv2
import numpy as np
from ultralytics import YOLO

from utils import capture_window

# ——— CONFIG ———

# Point this at your .pt file (string path relative to your project root)
MODEL_PATH = "runs/detect/shop_model_v2/weights/best.pt"
# If your weights really live under runs/detect/train/weights, do:
# MODEL_PATH = "runs/detect/train/weights/best.pt"

# Shop crop in the full window (x1, y1, x2, y2)
SHOP_ROI = (470, 941, 787, 1085)

# Detection confidence threshold
CONF_THRESHOLD = 0.4

# Title substring of your Bluestacks window
WINDOW_TITLE = "Bluestacks"
# ——————————

def detect_shop_once(model):
    # 1) grab the shop crop
    frame    = capture_window(WINDOW_TITLE)
    x1, y1, x2, y2 = SHOP_ROI
    shop_img = frame[y1:y2, x1:x2]

    gray     = cv2.cvtColor(shop_img, cv2.COLOR_BGR2GRAY)
    shop_img = np.stack([gray, gray, gray], axis=-1)  # shape: (H, W, 3)

    # shop_img = "data/screenshots/frame_1758246863_40.png" # test
    # 2) run YOLOv8
    results = model.predict(
        source=shop_img,
        conf=CONF_THRESHOLD,
        device="cpu",
        verbose=False
    )
    det = results[0]
    print("boxes:", det.boxes.xyxy.cpu().numpy())
    print("confs:", det.boxes.conf.cpu().numpy())
    print("cls_ids:", det.boxes.cls.cpu().numpy().astype(int))


    # 3) gather info
    cls_ids = det.boxes.cls.cpu().numpy().astype(int)
    names   = [model.names[c] for c in cls_ids]
    troops  = sorted(set(names))
    count   = len(names)

    # 4) print outcome
    if count:
        print(f"[{time.strftime('%H:%M:%S')}] Detected {count} items: {troops}")
    else:
        print(f"[{time.strftime('%H:%M:%S')}] No items detected in shop")

    # 5) annotate & save
    annotated = det.plot()  # draws boxes if present

    # if you want to overlay “no detections” text on a blank image:
    if count == 0:
        cv2.putText(
            annotated,
            "No detections",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
            cv2.LINE_AA
        )

    out_dir  = "runs/detect/shop_model_v2/saved"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"shop_{int(time.time())}.png")
    cv2.imwrite(out_path, annotated)
    print(f"  → saved annotated image to {out_path}\n")


def main():
    # sanity check
    if not os.path.isfile(MODEL_PATH):
        print(f"Error: weights file not found at '{MODEL_PATH}'")
        sys.exit(1)

    print(f"Loading model from: {MODEL_PATH}")
    model = YOLO(MODEL_PATH)

    try:
        while True:
            detect_shop_once(model)
            time.sleep(2)  # Wait 2 seconds before next detection
    except KeyboardInterrupt:
        print("🛑 Detection loop stopped by user.")



if __name__ == "__main__":
    main()