import os
import cv2
import time
import keyboard  # pip install keyboard
from utils import capture_window

# Settings
WINDOW_TITLE = "Bluestacks"
SAVE_DIR = "data/shop_data/raw_shop_data/data_set3"
SHOP_ROI = (470, 941, 787, 1085)  # (x1, y1, x2, y2)
FIELD_ROI = (477, 543, 833, 765)
SHOP_ROI = (402, 815, 678, 925)

# Make sure the folder exists
os.makedirs(SAVE_DIR, exist_ok=True)


def screenshot_capture():
    counter = 0
    print("Press 'S' to capture the shop panel (grayscale). Press 'Q' to quit.")

    while True:
        # Check if "S" is presseds
        if keyboard.is_pressed("s"):
            frame = capture_window(WINDOW_TITLE)

            cv2.imshow("window", frame)

            # Crop to shop region
            x1, y1, x2, y2 = SHOP_ROI
            shop_crop = frame[y1:y2, x1:x2]

            # Convert to grayscale
            # currently not in use
            gray_crop = cv2.cvtColor(shop_crop, cv2.COLOR_BGR2GRAY)

            # Filename: timestamp + counter
            filename = os.path.join(
                SAVE_DIR,
                f"shop_{int(time.time())}_{counter}.png"
            )

            cv2.imwrite(filename, shop_crop)
            print(f"[+] Saved shop sscreenshot: {filename}")

            counter += 1
            time.sleep(0.3)  # Prevent multiple triggers

        # Exit with "Q"
        if keyboard.is_pressed("q"):
            print("Exiting data collection.")
            break

if __name__ == "__main__":
    screenshot_capture()