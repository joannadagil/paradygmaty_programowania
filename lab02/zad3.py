def wczytaj_dane():
    N = int(input("Podaj liczbę ocen: "))
    oceny = []
    for i in range(N):
        ocena = int(input(f"Podaj ocenę {i+1} (0-100): "))
        oceny.append(ocena)
    return oceny

def oblicz_sume(numbers):
    # zwrócenie sumy elementów listy numbers
    return sum(numbers)

def oblicz_srednia(numbers):
    # zwrócenie średniej elementów listy dane lub 0 jeśli lista jest pusta
    return oblicz_sume(numbers)/len(numbers) if numbers else 0

def bubble_sort_malejący(numbers):
    # iteracja instrukcją sterującą pętlą for
    for i in range(len(numbers)-1):
        # iteracja zagnieżdzoną instrukcją sterującą pętlą for
        for j in range(len(numbers)-1-i):
            # porównanie dwóch sąsiednich elementów listy przy pomocy instrukcji warunkowej if
            if numbers[j] < numbers[j+1]:
                # zamiana miejscami dwóch sąsiednich elementów listy za pomocą przypisania wielokrotnego
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    # zwrócenie posortowanej listy numbers
    return numbers

def drukuj_wyniki(oceny, srednia):
    # wypisanie ocen powyżej średniej malejaco i ich liczby
    print("Oceny powyżej średniej posortowane malejąco:", end=' ')
    liczba = 0
    for ocena in oceny:
        if ocena > srednia:
            print(ocena, end=' ')
            liczba += 1

    print("")
    print("Liczba ocen powyżej średniej:", liczba)

def main():
    # wczytanie ocen
    oceny = wczytaj_dane()
    if not oceny:
        print("Brak danych.")
        return

    # obliczenie średniej ocen
    srednia = oblicz_srednia(oceny)

    # posortowanie listy ocen malejąco
    oceny_sorted = bubble_sort_malejący(oceny)

    # drukowanie wyników
    drukuj_wyniki(oceny_sorted, srednia)

# wywołanie funkcji main
if __name__ == "__main__":
    main()


