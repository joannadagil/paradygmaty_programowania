import threading
import time

def przetwarzaj_fragment(dane, start, end):
    global total
    fragment = dane[start:end]
    wynik = sum(fragment)
    with lock:
        total += wynik

if __name__ == "__main__":
    dane = list(range(1_000_000))
    n = len(dane)//4
    total = 0
    lock = threading.Lock()
    watki = []

    time_start = time.time()

    for i in range(4):
        t = threading.Thread(target=przetwarzaj_fragment, args=(dane, i*n, (i+1)*n))
        watki.append(t)
        t.start()

    for t in watki:
        t.join()
        
    time_end = time.time()

    print("Suma wszystkich elementów:", total)
    print("Czas wykonania:", time_end - time_start)

