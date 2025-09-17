import cv2
import numpy as np
from screen_capture import capture_window

def find_template(frame, template_path, threshold=0.8):
    """
    Look for a small image (template) inside the frame.
    Returns list of (x, y, w, h) for matches above threshold.
    """
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Template matching
    result = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)

    matches = []
    for pt in zip(*loc[::-1]):  # Switch x/y
        matches.append((pt[0], pt[1], w, h))

    return matches

if __name__ == "__main__":
    frame = capture_window("Google")  # capture Bluestacks
    matches = find_template(frame, "data/templates/elixir.png")

    # Draw rectangles around matches
    for (x, y, w, h) in matches:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Detected", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
