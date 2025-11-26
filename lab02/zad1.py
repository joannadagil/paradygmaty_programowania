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

def oblicz_sume(numbers):
    # zwrócenie sumy elementów listy dane
    return sum(numbers)

def oblicz_srednia(numbers):
    # zwrócenie średniej elementów listy dane lub 0 jeśli lista jest pusta
    return oblicz_sume(numbers)/len(numbers) if numbers else 0

def znajdz_min_max(numbers):
    # zwrócenie krotki (min, max) elementów listy dane lub (None, None) jeśli lista jest pusta
    return (min(numbers), max(numbers)) if numbers else (None, None)

def znajdz_mediane(numbers):
    # posortowanie listy numbers
    sorted_numbers = bubble_sort(numbers)
    n = len(sorted_numbers)
    if n == 0:
        return None
    mid = n // 2
    # zwrócenie mediany elementów listy numbers
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def bubble_sort(numbers):
    # iteracja instrukcją sterującą pętlą for
    for i in range(len(numbers)-1):
        # iteracja zagnieżdzoną instrukcją sterującą pętlą for
        for j in range(len(numbers)-1-i):
            # porównanie dwóch sąsiednich elementów listy przy pomocy instrukcji warunkowej if
            if numbers[j] > numbers[j+1]:
                # zamiana miejscami dwóch sąsiednich elementów listy za pomocą przypisania wielokrotnego
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    # zwrócenie posortowanej listy numbers
    return numbers

def drukuj_wyniki(dane):
    # wypisanie posortowanej listy numbers instrukcją wyjścia
    print("Posortowane dane:", dane)

def main():
    # wczytanie danych
    dane = wczytaj_dane()
    if not dane:
        print("Brak danych.")
        return
    # obliczene sumy, średniej, min i max, mediany
    srednia = oblicz_srednia(dane)
    min_val, max_val = znajdz_min_max(dane)
    mediana = znajdz_mediane(dane)
    # sortowanie danych
    posortowane = bubble_sort(dane)
    # drukowanie posortowanych danych
    drukuj_wyniki(posortowane)
    # drukowanie reszty wyników
    porównanie = '>' if mediana > srednia else '<' if mediana < srednia else '='
    print(f"Mediana vs średnia: {mediana} {porównanie} {srednia}")
    print(f"Średnia: {srednia}, Min: {min_val}, Max: {max_val}")

# wywołanie funkcji main
if __name__ == "__main__":
    main()


