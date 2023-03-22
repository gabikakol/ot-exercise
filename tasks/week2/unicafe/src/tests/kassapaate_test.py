import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.register = Kassapaate()

    def test_register_exists(self):
        self.assertEqual(self.register.money_in_register, 100000)

    def test_initial_lunches_count(self):
        self.assertEqual(self.register.cheap, 0)
        self.assertEqual(self.register.tasty, 0)      

    def test_enough_money_cheap(self):
        self.register.eat_cheap_cash(240)
        self.assertEqual(self.register.money_in_register, (100000+240))

    def test_enough_money_tasty(self):
        self.register.eat_tasty_cash(450)
        self.assertEqual(self.register.money_in_register, (100000+400))

    def test_not_enough_money_cheap(self):
        self.register.eat_cheap_cash(200)
        self.assertEqual(self.register.money_in_register, (100000))

    def test_not_enough_money_tasty(self):
        self.register.eat_tasty_cash(300)
        self.assertEqual(self.register.money_in_register, (100000))

    def test_enough_saldo_cheap(self):
        kortti = Maksukortti(1000)
        bool = self.register.eat_cheap_card(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(bool, True)
        self.assertEqual(self.register.cheap, 1)
        self.assertEqual(self.register.money_in_register, 100000)

    def test_not_enough_saldo_cheap(self):
        kortti = Maksukortti(100)
        bool = self.register.eat_cheap_card(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(bool, False)
        self.assertEqual(self.register.cheap, 0)
        self.assertEqual(self.register.money_in_register, 100000)    

    def test_enough_saldo_tasty(self):
        kortti = Maksukortti(1000)
        bool = self.register.eat_tasty_card(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(bool, True)
        self.assertEqual(self.register.tasty, 1)
        self.assertEqual(self.register.money_in_register, 100000)

    def test_not_enough_saldo_tasty(self):
        kortti = Maksukortti(100)
        bool = self.register.eat_tasty_card(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(bool, False)
        self.assertEqual(self.register.tasty, 0)
        self.assertEqual(self.register.money_in_register, 100000)

    def test_load_money_card(self):
        kortti = Maksukortti(200)
        self.register.load_money_card(kortti, 500)
        self.assertEqual(str(kortti), "Kortilla on rahaa 7.00 euroa")
        self.assertEqual(self.register.money_in_register, (100500))

    def test_load_money_card_empty(self):
        kortti = Maksukortti(200)
        sum = self.register.load_money_card(kortti, -1)
        self.assertEqual(sum, None)
        

    