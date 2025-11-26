"""
Moduł udostępnia funkcje do podstawowej analizy statystycznej list liczb.

Publiczne funkcje:
- mediana(numbers): zwraca medianę listy liczb.
- odchylenie_standardowe(numbers): zwraca odchylenie standardowe listy liczb.
"""

import sorting
import stats

def mediana(numbers):
    # posortowanie listy numbers
    sorted_numbers = sorting.sort(numbers)
    n = len(sorted_numbers)
    if n == 0:
        return None
    mid = n // 2
    # zwrócenie mediany elementów listy numbers
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def odchylenie_standardowe(numbers):
    # obliczenie średniej
    srednia = stats.oblicz_srednia(numbers)
    # obliczenie wariancji
    wariancja = sum((x - srednia) ** 2 for x in numbers) / len(numbers) if numbers else 0
    # zwrócenie odchylenia standardowego
    return wariancja ** 0.5