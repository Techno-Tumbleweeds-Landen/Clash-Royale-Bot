import cv2
import numpy as np
import pygetwindow as gw
import mss
from utils import capture_window

# === CONFIG ===
WINDOW_TITLE = "Bluestacks"
SCREENSHOT_PATH = "temp_screenshot.png"

clicks = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicks.append((x, y))
        print(f"🖱️ Clicked at: ({x}, {y})")
        if len(clicks) == 2:
            x1, y1 = clicks[0]
            x2, y2 = clicks[1]
            roi = img[y1:y2, x1:x2]
            cv2.imshow("🛒 Cropped Shop Panel", roi)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print(f"\n✅ Final SHOP_ROI = ({x1}, {y1}, {x2}, {y2})")
            print("Copy this into your detection script!")

img = capture_window(WINDOW_TITLE)
cv2.imwrite(SCREENSHOT_PATH, img)

cv2.imshow("🖼️ Click top-left and bottom-right of shop panel", img)
cv2.setMouseCallback("🖼️ Click top-left and bottom-right of shop panel", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()