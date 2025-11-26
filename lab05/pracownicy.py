class Pracownik:
    def pensja(self):
       return 0 
    
class Programista(Pracownik):
    def pensja(self): # nadpisanie metody
        return 10000

class Kierownik(Pracownik):
    def pensja(self): # nadpisanie metody
        return 15000

if __name__ == "__main__":
    pracownicy = [ Programista(), Programista(), Kierownik()]
    for p in pracownicy:
        print(p.pensja())
