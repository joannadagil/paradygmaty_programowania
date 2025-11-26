"""
Moduł udostępnia funkcje do wczytywania i wypisywania danych listowych.

Publiczne funkcje:
- wczytaj_dane(): wczytuje listę liczb od użytkownika.
- wypisz_dane(dane): wypisuje listę liczb na ekran.
"""
def wczytaj_dane():
    # pobranie ilości liczb przez instrukcję wejścia i przypisanie jej do zmiennej N
    N = int(input("Podaj liczbę elementów: "))
    # zainicjowanie pustej listy numbers
    numbers = []
    # iteracja instrukcją sterującą pętlą for i wczytanie N liczb do listy numbers przez instrukcję wejścia
    for i in range(N):
        number = float(input(f"Podaj liczbę {i+1}: "))
        numbers.append(number)
    # zwrócenie listy numbers
    return numbers


def wypisz_dane(dane):
    # wypisanie posortowanej listy numbers instrukcją wyjścia
    print("Posortowane dane:", dane)


