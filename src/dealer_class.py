from src.hand_class import Hand
class Dealer(Hand):
    def decide_hit_or_stand(self):
        return self.best_value() < 17  # house hits under 17