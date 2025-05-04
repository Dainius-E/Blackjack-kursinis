import unittest
from src.card_class import Card

class TestCardValue(unittest.TestCase):
    def test_number_card(self):
        c = Card('7', '♠')
        self.assertEqual(c.value(), [7])

    def test_face_card(self):
        for face in ('J','Q','K'):
            c = Card(face, '♦')
            self.assertEqual(c.value(), [10])

    def test_ace_card(self):
        c = Card('A', '♥')
        self.assertCountEqual(c.value(), [1, 11])

if __name__ == '__main__':
    unittest.main()