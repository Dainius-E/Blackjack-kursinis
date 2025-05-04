import json
import os
from src.blackjack_game_controller import BlackjackGame
from src.Shoe_class_with_Factory_method import StandardShoe_Factory_Method
from src.player_class import Player
from src.dealer_class import Dealer

CONFIG_FILE = "config.json"

def load_config():
    defaults = {"num_decks": 1}
    if not os.path.exists(CONFIG_FILE):
        return defaults
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {k: data.get(k, defaults[k]) for k in defaults}
    except (json.JSONDecodeError, IOError):
        return defaults

def save_config(config):
    # Overwrite the config.json 
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


if __name__ == "__main__":
    # 1) Load existing config
    cfg = load_config()
    print(f"Loaded configuration: {cfg['num_decks']} deck(s) by default.")

    # 2) If user inputs invalid argument, revert to default settings from config
    answer = input("Would you like to change the number of decks? [y/n]: ").strip().lower()
    if answer == 'y':
        nd = input("Enter number of decks to use (e.g. 1–8): ").strip()
        if nd.isdigit() and int(nd) > 0:
            cfg['num_decks'] = int(nd)
            save_config(cfg)
            print(f"Saved new default: {cfg['num_decks']} deck(s).")
        else:
            print("Invalid input, keeping previous number of decks.")


    game = BlackjackGame(num_decks=cfg['num_decks'],
                         shoe_factory=StandardShoe_Factory_Method())

    while True:
        game.play_round()
        again = input("\nPlay another round? [y/n]: ").strip().lower()
        if again != 'y':
            break
        game.player = Player("You")
        game.dealer = Dealer()