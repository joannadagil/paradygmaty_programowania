class Prostokat:
    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

    def pole(self):
        return self.szerokosc * self.wysokosc
    def obwod(self):
        return 2 * (self.szerokosc + self.wysokosc)
    def skaluj(self, faktor):
        self.szerokosc *= faktor
        self.wysokosc *= faktor

if __name__ == "__main__":
    s1 = Prostokat(3, 4)
    s2 = Prostokat(5, 6)
    
    print("Prostokąt 1 - pole:", s1.pole(), "obwód:", s1.obwod())
    print("Prostokąt 2 - pole:", s2.pole(), "obwód:", s2.obwod())

    s1.skaluj(2)
    print("Po skalowaniu Prostokąt 1 - pole:", s1.pole(), "obwód:", s1.obwod())
