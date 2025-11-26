class Student:
    def __init__(self, imie, nazwisko, oceny):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = oceny

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)
    def srednia(self):
        return sum(self.oceny) / len(self.oceny) if self.oceny else 0
    def info(self):
        print(f"Student {self.imie} {self.nazwisko} ma średnia: {self.srednia()}")


if __name__ == "__main__":
    s1 = Student("Aaa", "Aaaaa", [60, 70, 95])
    s2 = Student("Bbb", "Bbbbb", [40, 10])
    s3 = Student("Ccc", "Ccccc", [60, 70, 70, 60])
    
    s1.info()
    s2.info()
    s3.info()

    s3.dodaj_ocene(85)
    s3.info()

