#main
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
    state = GameState()
    controller = GameController()
    position = get_window_rect("Bluestacks")
    controller.window_left
    print(position)
    reader = ReadRegion(**info.regions)
    active = True

    while active:
        state.shop = reader.read_shop()
        state.elixir = reader.read_elixir()

        print(state.shop)
        print(state.elixir)

        for troop in state.shop:
            if troop and info.character_info[troop]["elixir"] <= state.elixir:
                # buy troop
                if troop == state.shop[0]:
                    controller.click_slot("LEFT")
                elif troop == state.shop[1]:
                    controller.click_slot("MIDDLE")
                elif troop == state.shop[2]:
                    controller.click_slot("RIGHT")
                    
        if state.elixir > 6:
            controller.click_slot("LEFT")
        time.sleep(3)


    #print(reader.read_shop())
