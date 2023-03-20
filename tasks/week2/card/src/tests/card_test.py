import unittest
from card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        print('set up goes here')

    def test_constructior_set_balance_correct(self):
        # inigialize a card with 10 eur (1000 cents)
        kortti = Card(1000)
        ans = str(kortti)

        self.assertEqual(ans, "Kortilla on rahaa 10.00 euroa")

    def test_saldo_cheap_correct(self):
        kortti = Card(1000)
        kortti.saldo_cheap()

        self.assertEqual(str(kortti), "Kortilla on rahaa 7.50 euroa")

# tbc @ 'a few points'