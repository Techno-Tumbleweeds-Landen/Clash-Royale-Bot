#utils
import pygetwindow as gw
import pyautogui
import numpy as np
import mss, cv2, time, os, keyboard
from exceptions import *

SHOP_ROI = (402, 815, 678, 925)
ELIXIR_ROI = (398, 974, 461, 1044)
ELIXIR_FRAME = (407, 984, 452, 1032)
LEFT_SHOP_FRAME = (117, 941, 192, 1037)

def click_at(x, y, button='left'):
    pyautogui.click(x, y, button=button)
    time.sleep(0.2)

def get_window_rect(title_substr):
    try:
            
        wins = gw.getWindowsWithTitle(title_substr)
        if not wins:
            raise RuntimeError("Window not found")
        win = wins[0]
        left, top = win.topleft
        dimensions = {
            "width": win.width,
            "height": win.height
        }
        if dimensions["width"] != 576 or dimensions["height"] != 1070:
            raise RuntimeError("Window size is not 576x1070")
        return {
            "left": left,
            "top": top,
            "width": win.width,
            "height": win.height
        }
    except Exception as e:
        print(f"[-] Exception found: {type(e).__name__}: {e}")
        raise WindowNotFound("Failed to find window containing:", title_substr)


def capture_window(title_substr):
    try:
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
            print("[+] Capture Successful")
            return img
    except Exception as e:
        print(f"[-] Exception found: {type(e).__name}: {e}")
        raise ScreenshotNotTaken("Failed to capture Screenshot")
        

def determine_roi(window_title, save_dir=None):
    window_name = "Select ROI - Click Top-Left and Bottom-Right"
    img = capture_window(window_title)

    if save_dir:
        cv2.imwrite(save_dir, img)

    clicks = []
    roi_result = {}

    def click_event(event, x, y, flags, param):
        nonlocal clicks, img, roi_result
        if event == cv2.EVENT_LBUTTONDOWN:
            clicks.append((x, y))
            print(f"Clicked at: ({x}, {y})")
            if len(clicks) == 2:
                x1, y1 = clicks[0]
                x2, y2 = clicks[1]
                # Normalize ordering
                x1n, x2n = sorted((int(x1), int(x2)))
                y1n, y2n = sorted((int(y1), int(y2)))
                roi = img[y1n:y2n, x1n:x2n].copy()
                cv2.imshow("Cropped ROI", roi)
                cv2.waitKey(0)
                cv2.destroyWindow("Cropped ROI")
                roi_result["roi"] = (x1n, y1n, x2n, y2n)
                print(f"Final ROI = ({x1n}, {y1n}, {x2n}, {y2n})")
                # close main window to finish interaction
                cv2.destroyWindow(window_name)

    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback(window_name, click_event)
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if "roi" not in roi_result:
        raise RuntimeError("ROI selection cancelled or incomplete")
    return roi_result["roi"]

def screenshot_collector(roi1, roi2, roi3, window_title="Bluestacks", save_dir="templates"):
    print("Press 'S' to capture region. Press 'Q' to quit.")
    os.makedirs(save_dir, exist_ok=True)
    counter = 0

    while True:
        if keyboard.is_pressed("s"):
            frame = capture_window(window_title) # captures full window
            x1, y1, x2, y2 = roi1 # unpacks roi
            
            shop_crop = frame[y1:y2, x1:x2] # crops to roi 

            filename = os.path.join(
                save_dir, 
                f"capture_{int(time.time())}_{counter}.png"
            ) # determines file name and location based on time and counter
            cv2.imwrite(filename, shop_crop) # saves file
            counter += 1 # adds one to counter
            print(f"Saved: {filename}") # prints saved file name
            time.sleep(0.3) # very simple debounce
        elif keyboard.is_pressed("d"):
            frame = capture_window(window_title) # captures full window
            x1, y1, x2, y2 = roi2 # unpacks roi
            
            shop_crop = frame[y1:y2, x1:x2] # crops to roi 

            filename = os.path.join(
                save_dir, 
                f"capture_{int(time.time())}_{counter}.png"
            ) # determines file name and location based on time and counter
            cv2.imwrite(filename, shop_crop) # saves file
            counter += 1 # adds one to counter
            print(f"Saved: {filename}") # prints saved file names
            time.sleep(0.3) # very simple debounce
        elif keyboard.is_pressed("f"):
            frame = capture_window(window_title) # captures full window
            x1, y1, x2, y2 = roi3 # unpacks roi
            
            shop_crop = frame[y1:y2, x1:x2] # crops to roi 

            filename = os.path.join(
                save_dir, 
                f"capture_{int(time.time())}_{counter}.png"
            ) # determines file name and location based on time and counter
            cv2.imwrite(filename, shop_crop) # saves file
            counter += 1 # adds one to counter
            print(f"Saved: {filename}") # prints saved file name
            time.sleep(0.3) # very simple debounce

        if keyboard.is_pressed("q"):
            print("Exiting image collector.") # prints exit message
            break # exits loopf

if __name__ == "__main__":
    # shop: (130, 923, 418, 1049)sd
    # left: (139, 938, 219, 1040)
    left = (139, 938, 219, 1040)
    middle = (236, 938, 316, 1040)
    right = (333, 938, 413, 1040)
    #determine_roi("Bluestacks")
    screenshot_collector(left, middle, right, save_dir="templates/cards")