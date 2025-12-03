#read_region
from utils import *
from game import *
import cv2

class ReadRegion:
    def __init__(self, **regions):
        self.ROI = regions
        self.FILE_PATH = "templates/unnamed_character.png"
        self.WINDOW_NAME = "Bluestacks"
        self.GameInfo = GameInfo()
        self.confidence = 0.8

    def read_elixir(self):
        game_sct = capture_window(self.WINDOW_NAME) # screenshots bluestacks
        x1, y1, x2, y2 = self.ROI["ELIXIR"] # unpacks the elixir region
        elixir_sct = game_sct[y1:y2, x1:x2] # crops the bluestacks screenshot

        gray_elixir_sct = cv2.cvtColor(elixir_sct, cv2.COLOR_BGR2GRAY) # converts to grayscale

        best_elixir = 10
        best_weight = 0

        # Check elixir values 0-10
        for elixir_value in range(11):
            template = cv2.imread(f"templates/elixirs/elixer{elixir_value:02d}.png", cv2.IMREAD_GRAYSCALE) # gets elixir template
            template_match = cv2.matchTemplate(gray_elixir_sct, template, cv2.TM_CCOEFF_NORMED) # matches template

            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(template_match)

            # Keep the highest confidence match
            if max_val >= self.confidence and max_val > best_weight:
                best_elixir = elixir_value
                best_weight = max_val

        return best_elixir



    def read_shop(self):
        game_sct = capture_window(self.WINDOW_NAME) # screenshots bluestacks
        x1, y1, x2, y2 = self.ROI["SHOP"] # unpacks the shop region
        shop_sct = game_sct[y1:y2, x1:x2] # crops the bluestacks screenshot

        gray_shop_sct = cv2.cvtColor(shop_sct, cv2.COLOR_BGR2GRAY) # converts to grayscale

        shop_characters = [None, None, None]
        shop_weights = [None, None, None]

        for character in self.GameInfo.characters:
            template = cv2.imread(f"templates/cards/{character}.png", cv2.IMREAD_GRAYSCALE) # gets character template
            template_match = cv2.matchTemplate(gray_shop_sct, template, cv2.TM_CCOEFF_NORMED) # matches template

            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(template_match)

            region_width = x2 - x1 # find region width

            # Get x-coordinate of the match location
            match_x = max_loc[0]

            # Determine position
            if max_val >= self.confidence:
                # First shop slot
                if match_x < region_width / 3:
                    # If it hasn't found a match yet
                    if shop_characters[0] == None:
                        shop_characters[0] = character
                        shop_weights[0] = max_val
                    # if it has found a match already, it keeps the higher weighted one
                    else: 
                        if max_val > shop_weights[0]:
                            shop_characters[0] = character

                # Second shop slot
                elif match_x < 2 * region_width / 3:
                    if shop_characters[1] == None:
                        shop_characters[1] = character
                        shop_weights[1] = max_val
                    else: 
                        if max_val > shop_weights[1]:
                            shop_characters[1] = character
                
                # Last shop slot
                else:
                    if shop_characters[2] == None:
                        shop_characters[2] = character
                        shop_weights[2] = max_val
                    else: 
                        if max_val > shop_weights[2]:
                            shop_characters[2] = character
        return shop_characters

        
