import random
from abc import ABC, abstractmethod
from src.deck_class import Deck
from src.card_class import Card
import time
class Shoe_Factory_method(ABC):
    @abstractmethod
    def build_cards(self, num_decks: int) -> list:
        ...
class StandardShoe_Factory_Method(Shoe_Factory_method):
    def build_cards(self, num_decks: int) -> list:
        cards = []
        for _ in range(num_decks):
            for r in Deck.ranks:
                for s in Deck.suits:
                    cards.append(Card(r, s))
        return cards

class Shoe:
    def __init__(self, num_decks: int = 1, factory: Shoe_Factory_method = StandardShoe_Factory_Method()):
        self.num_decks = num_decks
        self._cards = factory.build_cards(num_decks)
        random.shuffle(self._cards)

    def deal_one(self):
        return self._cards.pop() if self._cards else None

    def cards_left(self):
        return len(self._cards)