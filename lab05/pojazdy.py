class Pojazd:
    def __init__(self, marka):
        self.marka = marka
    def info(self):
        print(f"Pojazd marki {self.marka}")
    def uruchom(self):
        print("Uruchamiam pojazd...")

class PojazdSilnikowy(Pojazd):
    def uruchom(self): # przesłonięcie metody z klasy bazowej
        print("Uruchamiam pojazd silnikowy...")

class Motocykl(PojazdSilnikowy):
    def __init__(self, marka, pojemnosc):
        super().__init__(marka)
        self.pojemnosc = pojemnosc
    def info(self): # przesłonięcie metody z klasy bazowej
        print(f"Motocykl: {self.marka}, pojemność: {self.pojemnosc}cc")

class Samochod(PojazdSilnikowy):
    def __init__(self, marka, liczba_drzwi):
        super().__init__(marka)
        self.liczba_drzwi = liczba_drzwi
    def info(self): # przesłonięcie metody z klasy bazowej
        print(f"Samochód: {self.marka}, drzwi: {self.liczba_drzwi}")

class Rower(Pojazd):
    def __init__(self, marka, typ):
        super().__init__(marka)
        self.typ = typ
    def info(self): # przesłonięcie metody z klasy bazowej
        print(f"Rower {self.marka}, typ: {self.typ}")

if __name__ == "__main__":
    pojazdy = [ Samochod("Toyota", 5), Rower("Merida", "górski"), Samochod("BMW", 3), Motocykl("Yamaha", 600) ] 
    for p in pojazdy:
        p.info()
        p.uruchom()
