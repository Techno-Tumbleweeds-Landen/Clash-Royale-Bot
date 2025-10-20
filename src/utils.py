import pygetwindow as gw
import mss
import numpy as np
import cv2

def get_window_rect(title_substr):
    wins = gw.getWindowsWithTitle(title_substr)
    if not wins:
        raise RuntimeError("Window not found")
    win = wins[0]
    left, top = win.topleft
    a = {
        "width": win.width,
        "height": win.height
    }
    print(a)
    return {
        "left": left,
        "top": top,
        "width": win.width,
        "height": win.height
    }

def capture_window(title_substr):
    region = get_window_rect(title_substr)
    with mss.mss() as sct:
        monitor = {
            "left": region["left"],
            "top": region["top"],
            "width": region["width"],
            "height": region["height"]
        }

        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        #gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         
        return img
