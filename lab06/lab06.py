from functools import reduce
import random

def przetworz_liczby(lista):
    return list(map(lambda x: x*x, (list(filter(lambda x: x % 2 == 0, lista)))))

def suma(x, y): return x + y
def iloczyn(x, y): return x * y
def maksimum(x, y): return x if x > y else y

def agreguj(lista, funkcja_agregujaca):
    return reduce(funkcja_agregujaca, lista)

def stworz_filtr(min, max):
    def filtr(x):
        return min <= x and x <= max
    return filtr

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Oryginalne liczby:    ", lista)
    print("-------------- ZADANIE 1 --------------")
    print("Przetworzone liczby:  ", przetworz_liczby(lista))
    print("-------------- ZADANIE 2 --------------")
    print("Agregacja sumowaniem: ", agreguj(lista, suma))
    print("Agregacja iloczynem:  ", agreguj(lista, iloczyn))
    print("Agregacja maksowaniem:", agreguj(lista, maksimum))
    print("-------------- ZADANIE 3 --------------")
    duza_lista = [random.randint(1,100) for _ in range(10000)]
    print("Przed filtrowaniem: ", len(duza_lista))
    print("Po filtrowaniu:     ", len(list(filter(stworz_filtr(30,70), duza_lista))))