class BankKonto:
    def __init__(self, nr, saldo=0.0):
        self.numer_konta = nr
        self.saldo = saldo

    def wplac(self, kwota):
        if kwota > 0:
            self.saldo += kwota
            return True
        return False

    def wyplac(self, kwota):
        if 0 < kwota <= self.saldo:
            self.saldo -= kwota
            return True
        return False

    def saldo(self):
        return self.saldo

if __name__ == "__main__":
    konto = BankKonto("1234", 1000.0)
    print("Saldo początkowe:", konto.saldo)
    konto.wplac(500.0)
    print("Saldo po wpłacie 500.0:", konto.saldo)
    konto.wyplac(200.0)
    print("Saldo po wypłacie 200.0:", konto.saldo)
    sukces = konto.wyplac(2000.0)
    print("Próba wypłaty 2000.0:", "Sukces" if sukces else "Niepowodzenie")
    print("Saldo końcowe:", konto.saldo)