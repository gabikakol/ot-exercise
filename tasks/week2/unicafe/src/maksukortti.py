class Maksukortti:
    def __init__(self, saldo):
        # saldo in cents
        self.saldo = saldo

    def load_money(self, amount):
        self.saldo += amount

    def spend_money(self, amount):
        if self.saldo < amount:
            return False

        self.saldo = self.saldo - amount
        return True

    def __str__(self):
        saldo_eur = round(self.saldo / 100, 2)

        return "Kortilla on rahaa {:0.2f} euroa".format(saldo_eur)
