import unittest
from src.hand_class import Hand
from src.card_class import Card

class TestHandBestValue(unittest.TestCase):
    def setUp(self):
        self.h = Hand()

    def test_simple_total(self):
        self.h.add_card(Card('5','♣'))
        self.h.add_card(Card('9','♦'))
        self.assertEqual(self.h.best_value(), 14)

    def test_ace_low_high(self):
        self.h.add_card(Card('A','♣'))
        self.h.add_card(Card('9','♦'))
        # should pick 20 instead of 10
        self.assertEqual(self.h.best_value(), 20)

    def test_multiple_aces(self):
        for _ in range(2):
            self.h.add_card(Card('A','♠'))
        self.h.add_card(Card('9','♥'))
        # Totals: {11, 21, 31}, so best is 21
        self.assertEqual(self.h.best_value(), 21)

    def test_bust(self):
        for r in ('K','Q','5'):
            self.h.add_card(Card(r,'♠'))
        self.assertTrue(self.h.is_bust())

if __name__ == '__main__':
    unittest.main()
