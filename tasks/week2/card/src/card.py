CHEAP = 250
TASTY = 400


class Card:
    def __init__(self, saldo):
        # saldo in cents
        self.saldo = saldo

    def saldo_cheap(self):
        if self.saldo >= CHEAP:
            self.saldo -= CHEAP

    def saldo_tasty(self):
        if self.saldo >= TASTY:
            self.saldo -= TASTY

    def load_money(self, amount):
        if amount < 0:
            return

        self.saldo += amount

        if self.saldo > 15000:
            self.saldo = 15000

    def __str__(self):
        saldo_eur = round(self.saldo / 100, 2)

        return "Kortilla on rahaa {:0.2f} euroa".format(saldo_eur)
