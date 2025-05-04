from src.card_class import Card
class Hand:
    def __init__(self):
        self._cards = []

    def add_card(self, card):
        self._cards.append(card)

    def values(self):
        totals = [0]
        for card in self._cards:
            new_totals = []
            for v in card.value():
                for t in totals:
                    new_totals.append(t + v)
            totals = set(new_totals)
        return totals

    def best_value(self):
        valid = [v for v in self.values() if v <= 21]
        return max(valid) if valid else min(self.values())

    def is_bust(self):
        return min(self.values()) > 21