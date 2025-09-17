import mss
import numpy as np
from get_window import get_window_rect

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
        return np.array(img)[:, :, :3]
print(capture_window("Google"))