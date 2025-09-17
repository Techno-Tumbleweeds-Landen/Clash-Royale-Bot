import pygetwindow as gw

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
