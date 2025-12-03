#game
import pyautogui
import time
from utils import get_window_rect

class GameInfo:
    def __init__(self):
        self.characters = (
            "archer_queen", "bandit", "barbarian", "dart_goblin", "electro_giant",
            "executioner", "goblin", "goblin_machine", "golden_knight",
            "mega_knight", "mini_pekka", "monk", "musketeer", "pekka", "princess",
            "prince", "royal_giant", "royal_ghost", "spear_goblin", "skeleton_dragons",
            "skeleton_king", "valkyrie", "witch", "wizard")
        
        self.character_info = {
            # 2 Elixir
            "mini_pekka": {"elixir": 2, "traits": ["pekka", "brutalist"]},
            "goblin": {"elixir": 2, "traits": ["goblin", "assassin"]},
            "spear_goblin": {"elixir": 2, "traits": ["goblin", "blaster"]},
            "barbarian": {"elixir": 2, "traits": ["brawler", "clan"]},
            "skeleton_dragons": {"elixir": 2, "traits": ["ranger", "undead"]},
            "wizard": {"elixir": 2, "traits": ["blaster", "clan"]},
            "royal_giant": {"elixir": 2, "traits": ["giant", "ranger"]},

            # 3 Elixir
            "valkyrie": {"elixir": 3, "traits": ["brutalist", "clan"]},
            "pekka": {"elixir": 3, "traits": ["brawler", "pekka"]},
            "prince": {"elixir": 3, "traits": ["noble", "brawler"]},
            "dart_goblin": {"elixir": 3, "traits": ["goblin", "ranger"]},
            "electro_giant": {"elixir": 3, "traits": ["giant", "superstar"]},
            "musketeer": {"elixir": 3, "traits": ["noble", "superstar"]},
            "executioner": {"elixir": 3, "traits": ["ace", "blaster"]},

            # 4 Elixir
            "witch": {"elixir": 4, "traits": ["undead", "superstar"]},
            "mega_knight": {"elixir": 4, "traits": ["ace", "brawler"]},
            "princess": {"elixir": 4, "traits": ["noble", "blaster"]},
            "royal_ghost": {"elixir": 4, "traits": ["assassin", "undead"]},
            "bandit": {"elixir": 4, "traits": ["ace", "assassin"]},
            "goblin_machine": {"elixir": 4, "traits": ["goblin", "brutalist"]},

            # 5 Elixir
            "golden_knight": {"elixir": 5, "traits": ["noble", "assassin"]},
            "skeleton_king": {"elixir": 5, "traits": ["undead", "brutalist"]},
            "archer_queen": {"elixir": 5, "traits": ["clan", "ranger"]},
            "monk": {"elixir": 5, "traits": ["ace", "superstar"]},
        }

        self.regions = {
            "SHOP": (130, 923, 418, 1049),
            "ELIXIR": (437, 974, 487, 1044)
        }

class GameState:
    def __init__(self):
        self.player_health = 10
        self.elixir = 4
        self.shop = [None, None, None]

class GameController:
    def __init__(self, window_title="Bluestacks"):
        # Get the Bluestacks window position on the desktop
        rect = get_window_rect(window_title)
        self.window_left = rect["left"]
        self.window_top = rect["top"]

        # Positions are stored as coordinates relative to the top-left of the emulator window.
        # Define relative positions (same values you used before)
        relative_positions = {
            "LEFT": (178, 986),
            "MIDDLE": (274, 986),
            "RIGHT": (370, 986)
        }

        # Convert relative positions to absolute screen coordinates
        self.card_positions = {
            "LEFT": (178+self.window_left, 986+self.window_top),
            "MIDDLE": (274+self.window_left, 986+self.window_top),
            "RIGHT": (370+self.window_left, 986+self.window_top)
        }


    def click_slot(self, slot_name, button='left'):
        x, y = self.card_positions[slot_name]
        self.click_at(x, y, button=button)

    def click_at(self, x, y, button='left'):
        pyautogui.click(x, y, button=button)
        time.sleep(0.2)

