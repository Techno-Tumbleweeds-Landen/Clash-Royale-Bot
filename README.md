# Merge Tactics Bot

Detect items in the Merge Tactics shop using OpenCV template matching and screenshots from a Bluestacks emulator using mss.

## How It Works

1. Finds Bluestacks and takes a screenshot.
2. Crops the image to only the shop and converts to grayscale
3. Runs openCV's template matching and finds matches using minMaxLoc()
4. prints the 3 characters in the shop.
5. prints the amount of elixer the player has.
6. Buys the first available card in the shop.

## Scripts

- `main.py`: This is the main program that creates instances of our classes and runs our program
- `game.py`: Contains 3 classes, one to hold static info, another to hold game state, and another to make actions
- `read_region.py`: Creates a class with a read_shop method that returns the 3 characters in the shop
- `utils.py`: Useful functions for project development and project use
- `exceptions.py`: has two empty classes so I can throw my own exceptions

## What's next

Add logic to the game so it makes smart decisions. I think a decision tree would be ideal for this.

## Requirements

- Packages: `opencv-python`, `mss`, `keyboard`, `pygetwindow`, `numpy`, `pyautogui`

## Install
python -m venv .venv

.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

### Note

in utils:

- determine_roi() and screenshot_collector() are both AI generated, as they were originally meant for debugging