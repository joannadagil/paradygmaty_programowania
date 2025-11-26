# zdefiniowanie funkcji main
def main():
    # pobranie ilości liczb przez instrukcję wejścia i przypisanie jej do zmiennej N
    N = int(input('Podaj ilość liczb do sortowania: '))
    # zainicjowanie pustej listy numbers
    numbers = []
    # iteracja instrukcją sterującą pętlą for i wczytanie N liczb do listy numbers przez instrukcję wejścia
    for i in range(N):
        number = float(input(f'Podaj {i+1} liczbę: '))
        numbers.append(number)
    # iteracja instrukcją sterującą pętlą for
    for i in range(N-1):
        # iteracja zagnieżdzoną instrukcją sterującą pętlą for
        for j in range(N-1-i):
            # porównanie dwóch sąsiednich elementów listy przy pomocy instrukcji warunkowej if
            if numbers[j] > numbers[j+1]:
                # zamiana miejscami dwóch sąsiednich elementów listy za pomocą przypisania wielokrotnego
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    # wypisanie posortowanej listy numbers instrukcją wyjścia
    print(numbers)
    pass

# wywołanie funkcji main
if __name__ == '__main__':
    main()