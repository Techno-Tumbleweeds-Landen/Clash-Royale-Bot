from utils import *
from read_region import *
from game import *
import cv2

# TODO: capture image and crop region of interest
# TODO: save images to directory and name by card
# TODO: write script to go through each card template
# and search the shop for that template, then make 
# a list

# WINDOW SIZE NEEDED
# {'width': 576, 'height': 1070}

if __name__ == "__main__":
    info = GameInfo()

    reader = ReadRegion(**info.regions)

    print(reader.read_shop())
