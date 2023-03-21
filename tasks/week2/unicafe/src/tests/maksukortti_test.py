import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_card_exists(self):
        self.assertNotEqual(self.kortti, None)
    
    def test_card_initial_balance(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_load_money(self):
        self.kortti.load_money(2000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 30.00 euroa")

    def test_spend_money_enough(self):
        self.kortti.spend_money(500)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 5.00 euroa")

    def test_spend_money_not_enough(self):
        self.kortti.spend_money(5000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_spend_money_true(self):
        self.assertEqual(self.kortti.spend_money(500), True)

    def test_spend_money_false(self):
        self.assertEqual(self.kortti.spend_money(5000), False)