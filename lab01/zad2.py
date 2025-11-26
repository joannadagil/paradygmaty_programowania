# zdefiniowanie funkcji main
def main():
    # pobranie liczby N przez instrukcję wejścia i przypisanie jej do zmiennej N
    N = int(input('Podaj liczbę N: '))
    # iteracja instrukcją sterującą pętlą while dopóki N jest większe od 0
    while N > 0:
        # wypisanie aktualnej wartości N instrukcją wyjścia
        print(N, end=' ')
        # zmniejszenie wartości N o 1
        N -= 1
    # wypisanie pustej linii instrukcją wyjścia (w celach estetycznych)
    print('')
    pass

# wywołanie funkcji main
if __name__ == '__main__':
    main()