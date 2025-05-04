import unittest
from src.Shoe_class_with_Factory_method import Shoe

class TestShoe(unittest.TestCase):
    def test_deck_count(self):
        shoe = Shoe(num_decks=3)
        # 3 decks × 52 cards each
        self.assertEqual(shoe.cards_left(), 3 * 52)

    def test_exhaustion(self):
        shoe = Shoe(num_decks=1)
        # draw all 52 cards
        for _ in range(52):
            self.assertIsNotNone(shoe.deal_one())
        # now it’s empty
        self.assertIsNone(shoe.deal_one())
        self.assertEqual(shoe.cards_left(), 0)

if __name__ == '__main__':
    unittest.main()
