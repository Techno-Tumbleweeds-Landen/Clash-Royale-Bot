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

        img = sct.grab(monitor)
        frame = np.frombuffer(img.rgb, dtype=np.uint8).copy()
        frame = frame.reshape((img.height, img.width, 3))
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        return frame
