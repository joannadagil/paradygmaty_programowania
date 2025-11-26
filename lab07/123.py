import time

def suma_lista(lista, i=0):
    if i == len(lista):
        return 0
    return lista[i] + suma_lista(lista, i+1)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib_tail(n, last=1, lastlast=0):
    if n == 1: return last
    return fib_tail(n-1, last+lastlast, last)

def liczby_pierwsze():
    n = 2
    while True:
        ok = True
        for i in range(2,n):
            if n % i == 0:
                ok = False
                break
        if ok: yield n
        n += 1

if __name__ == "__main__":
    print("-------------- ZADANIE 1 --------------")
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("lista:   ", lista)
    print("suma_lista(lista):  ", suma_lista(lista))
    print("-------------- ZADANIE 2 --------------")
    time3 = time.time()
    res = fib_tail(35)
    time4 = time.time()
    print("fib_tail(35):", res, ", time: ", (time4-time3) * 1000000)
    time1 = time.time()
    res = fib(35)
    time2 = time.time()
    print("fib(35):     ", res, ", time: ", (time2-time1) * 1000000)
    print("-------------- ZADANIE 3 --------------")
    gen = liczby_pierwsze()
    for _ in range(20):
        print(next(gen), end=" ")
    print()




