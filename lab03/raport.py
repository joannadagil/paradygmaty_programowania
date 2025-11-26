"""
Moduł udostępnia funkcje do stworzenia raportu z analizy listy liczb.

Publiczne funkcje:
- zapisz_raport(srednia, min_val, max_val, mediana, odchylenie, porownanie, filename="raport.txt"): zapisuje raport do pliku tekstowego.
"""
def zapisz_raport(srednia, min_val, max_val, mediana, odchylenie, porownanie, filename="raport.txt"):
    # zapisuje raport do pliku tekstowego.
    
    with open(filename, "w") as f:
        f.write("Raport:\n")
        f.write(f"Srednia: {srednia}\n")
        f.write(f"Min: {min_val}\n")
        f.write(f"Max: {max_val}\n")
        f.write(f"Mediana: {mediana}\n")
        f.write(f"Odchylenie standardowe: {odchylenie}\n")
        f.write(f"Mediana vs srednia: {mediana} {porownanie} {srednia}\n")
