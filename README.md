# Merge Tactics Bot

Detect items in the Merge Tactics shop using OpenCV template matching and screenshots from a Bluestacks emulator.

## How It Works

1. Finds Bluestacks and takes a screenshot.
2. Crops the image to only the shop and converts to grayscale
3. Runs openCV's template matching and finds matches using minMaxLoc()
4. prints the 3 characters in the shopcted shop items.

## Scripts

- `main.py`: This is the main program that creates instances of our classes and runs our program
- `game.py`: Contains 3 classes, one to hold static info, another to hold game state, and another to make actions
- `read_region.py`: Creates a class with a read_shop method that returns the 3 characters in the shop
- `utils.py`: Useful functions for project development and project use

## What's next

1. Use template matching to read bench and field
2. store game state
3. hopefully create a neural network and train it to make decisions for the game

## Requirements

- Packages: `opencv-python`, `mss`, `keyboard`, `pygetwindow`, `numpy`

## Install
python -m venv .venv

.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

### Note

in utils:

- determine_roi() and screenshot_collector() are both AI generated, as they were originally meant for debugging