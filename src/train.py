from ultralytics import YOLO

# 1. Load pretrained nano model
model = YOLO("yolov8n.pt")

# 2. Train on your local Roboflow export
model.train(
    data="data/shop_data/labeled_shop_data/data.yaml",  # relative path to your data.yaml
    epochs=50,                                    # number of training epochs
    imgsz=640,                                    # image size
    batch=16                                      # adjust to your GPU/CPU capacity
)

# 3. Save is under runs/train/exp