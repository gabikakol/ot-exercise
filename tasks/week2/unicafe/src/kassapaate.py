class Kassapaate:
    def __init__(self):
        self.money_in_register = 100000
        self.cheap = 0
        self.tasty = 0

    def eat_cheap_cash(self, maksu):
        if maksu >= 240:
            self.money_in_register = self.money_in_register + 240
            self.cheap += 1
            return maksu - 240
        else:
            return maksu

    def eat_tasty_cash(self, maksu):
        if maksu >= 400:
            self.money_in_register = self.money_in_register + 400
            self.tasty += 1
            return maksu - 400
        else:
            return maksu

    def eat_cheap_card(self, kortti):
        if kortti.saldo >= 240:
            kortti.spend_money(240)
            self.cheap += 1
            return True
        else:
            return False

    def eat_tasty_card(self, kortti):
        if kortti.saldo >= 400:
            kortti.spend_money(400)
            self.tasty += 1
            return True
        else:
            return False

    def load_money_card(self, kortti, sum):
        if sum >= 0:
            kortti.load_money(sum)
            self.money_in_register += sum
        else:
            return
