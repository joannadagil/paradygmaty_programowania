"""
Główny moduł programu do analizy listy liczb.
"""
import utils
import sorting
import stats
import analityka
import raport

def main():
    # wczytanie danych
    dane = utils.wczytaj_dane()
    if not dane:
        print("Brak danych.")
        return
    # obliczene sumy, średniej, min i max, mediany
    srednia = stats.oblicz_srednia(dane)
    min_val, max_val = stats.znajdz_min_max(dane)
    mediana = analityka.mediana(dane)
    odchylenie = analityka.odchylenie_standardowe(dane)
    # sortowanie danych
    posortowane = sorting.sort(dane)
    # drukowanie posortowanych danych
    utils.wypisz_dane(posortowane)
    # drukowanie reszty wyników
    porównanie = '>' if mediana > srednia else '<' if mediana < srednia else '='
    print(f"Mediana vs średnia: {mediana} {porównanie} {srednia}")
    print(f"Średnia: {srednia}, Min: {min_val}, Max: {max_val}")
    print(f"Mediana: {mediana}, Odchylenie standardowe: {odchylenie}")
    # zapisanie raportu do pliku
    raport.zapisz_raport(srednia, min_val, max_val, mediana, odchylenie, porównanie)

# wywołanie funkcji main
if __name__ == "__main__":
    main()


