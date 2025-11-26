"""
Moduł udostępnia funkcje do sortowania listy liczb.

Publiczne funkcje:
- sort(numbers): zwraca posortowoną listy liczb.
"""
def sort(numbers):
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