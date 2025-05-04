from src.hand_class import Hand
class Player(Hand):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def decide_hit_or_stand(self):
        while True:
            choice = input(f"{self.name}, Hit or Stand? [h/s]: ").strip().lower()
            if choice in ('h','s'):
                return choice == 'h'