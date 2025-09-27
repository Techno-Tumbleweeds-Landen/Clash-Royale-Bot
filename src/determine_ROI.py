import cv2
import numpy as np
import pygetwindow as gw
import mss

# === CONFIG ===
WINDOW_TITLE = "Bluestacks"
SCREENSHOT_PATH = "temp_screenshot.png"

# === Step 1: Capture Bluestacks Window ===
def capture_bluestacks():
    win = gw.getWindowsWithTitle(WINDOW_TITLE)[0]
    bbox = (win.left, win.top, win.right, win.bottom)
    with mss.mss() as sct:
        monitor = {
            "left": bbox[0],
            "top": bbox[1],
            "width": bbox[2] - bbox[0],
            "height": bbox[3] - bbox[1]
        }
        img = np.array(sct.grab(monitor))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        cv2.imwrite(SCREENSHOT_PATH, img)
        return img

# === Step 2: Click to Define ROI ===
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

# === Run ===
img = capture_bluestacks()
cv2.imshow("🖼️ Click top-left and bottom-right of shop panel", img)
cv2.setMouseCallback("🖼️ Click top-left and bottom-right of shop panel", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()