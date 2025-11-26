"""
Moduł udostępnia funkcje do najbardziej podstawowej analizy statystycznej list liczb.

Publiczne funkcje:
- oblicz_srednia(numbers): zwraca średnią listy liczb.
- znajdz_min_max(numbers): zwraca krotkę (min, max) listy liczb.
"""
def _oblicz_sume(numbers):
    # zwrócenie sumy elementów listy dane
    return sum(numbers)

def oblicz_srednia(numbers):
    # zwrócenie średniej elementów listy dane lub 0 jeśli lista jest pusta
    return _oblicz_sume(numbers)/len(numbers) if numbers else 0


def znajdz_min_max(numbers):
    # zwrócenie krotki (min, max) elementów listy dane lub (None, None) jeśli lista jest pusta
    return (min(numbers), max(numbers)) if numbers else (None, None)


