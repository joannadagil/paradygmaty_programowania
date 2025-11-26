# zdefiniowanie funkcji main
def main():
    # pobranie liczby N przez instrukcję wejścia i przypisanie jej do zmiennej N
    N_str = input('Podaj liczbę całkowitą N: ')
    # sprawdzenie czy N jest liczba całkowitą przez instrukcję sterującą warunkową if
    if N_str.lstrip('-').isdigit():
        N = int(N_str)
    else:
        print("Błąd: N musi być liczbą całkowitą!")
        return
    # zainicjowanie zmiennej wynikowej suma
    suma = 0
    # iteracja po liczbach parzystych od 0 do N włącznie instrukcją sterującą pętlą for
    for i in range(0, N + 1, 2):
        # dodanie kolejnej liczby parzystej do sumy
        suma += i
    # wypisanie wyniku instrukcją wyjścia
    print(f"Suma liczb parzystych od 0 do {N} wynosi {suma}")
    pass

# wywołanie funkcji main
if __name__ == '__main__':
    main()