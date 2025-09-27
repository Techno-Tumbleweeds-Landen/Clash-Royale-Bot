# Merge Tactics Bot

Detect items in the Merge Tactics shop using YOLOv8 and screenshots from a Bluestacks emulator.

## How It Works

1. Finds Bluestacks and takes a screenshot.
2. Crops the image to only the shop and converts to grayscale
3. Runs YOLOv8n inference on the processed image.
4. Saves annotated images showing detected shop items.

## Scripts

- `data_collector.py`: Only used to gather screenshots of the game for training the model.
- `detect_shop.py`: Used to test the shop model.
- `determine_ROI.py`: Was used to determine to region of interest i.e. shop
- `train.py`: Trains a YOLOv8n model on data after labeling it in roboflow
- `utils.py`: Functions to get location of Bluestacks window and to take a screenshot

## What's next

1. train model to read the bench
2. train model to read the field
3. find python library to use to control the game
4. create main game logic

## Requirements

- Packages: `ultralytics`, `opencv-python`, `mss`, `keyboard`, `pygetwindow`, `numpy`

### Install
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

### Note

Most of the code for training, testing, and gathering the data **so far** was ai generated.
This is a very big project with so many new things and it has taught me so much already.
Now that I have an understanding of how roboflow works, with creating models and labeling data
I have the knowledge to do it myself, so for training the bench and field models, I will train 
and code the bench and field models without relying on AI.