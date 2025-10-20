from utils import *
import cv2

# TODO: capture image and crop region of interest
# TODO: save images to directory and name by card
# TODO: write script to go through each card template
# and search the shop for that template, then make 
# a list

# WINDOW SIZE NEEDED
# {'width': 576, 'height': 1070}


screenshot = capture_window("Bluestacks")


ICON_FRAME = (117, 941, 192, 1037)
SHOP_REGION = (100, 923, 387, 1049)
x1, y1, x2, y2 = SHOP_REGION
FILE_PATH = "templates/unnamed_character.png"
template = cv2.imread("templates/cards/spear_goblin.png", cv2.IMREAD_GRAYSCALE)
shop_crop = screenshot[y1:y2, x1:x2]
gray_shop = cv2.cvtColor(shop_crop, cv2.COLOR_BGR2GRAY)

template_match = cv2.matchTemplate(gray_shop, template, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(template_match)

# Get width of the shop region
region_width = x2 - x1

# Get x-coordinate of the match location
match_x = max_loc[0]

# Determine position
if match_x < region_width / 3:
    position = "left"
elif match_x < 2 * region_width / 3:
    position = "middle"
else:
    position = "right"

print(f"Max Value: {max_val}")
print(f"Match found in the {position} slot.")
