import unittest
from card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.kortti = Card(1000)

    def test_constructior_set_balance_correct(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldo_cheap(self):
        self.kortti.saldo_cheap()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.50 euroa")

    def test_saldo_tasty(self):
        self.kortti.saldo_tasty()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_saldo_cheap_negative_balance(self):
        kortti = Card(200)
        kortti.saldo_cheap()
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_saldo_tasty_negative_balance(self):
        kortti = Card(300)
        kortti.saldo_tasty()
        self.assertEqual(str(kortti), "Kortilla on rahaa 3.00 euroa")

    def test_card_load_money_positive(self):
        self.kortti.load_money(2500)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa")

    def test_card_load_money_negative(self):
        self.kortti.load_money(-500)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_card_saldo_exceeds_maximum(self):
        self.kortti.load_money(20000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150.00 euroa")