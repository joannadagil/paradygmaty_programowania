from multiprocessing import Process, Queue, cpu_count
import time

def przetwarzaj(dane, start, end, totals):
    fragment = dane[start:end]
    wynik = sum(fragment)
    totals.put(wynik)

if __name__ == "__main__":
    dane = list(range(1_000_000))
    count = cpu_count()
    n = len(dane) // count
    totals = Queue()
    total = 0
    procesy = []

    time_start = time.time()

    for i in range(count):
        p = Process(target=przetwarzaj, args=(dane, i*n, (i+1)*n if i < count-1 else len(dane), totals))
        procesy.append(p)
        p.start()

    for p in procesy:
        p.join()

    while not totals.empty():
        total += totals.get()

    time_end = time.time()

    print("Suma wszystkich elementów:", total)
    print("Czas wykonania:", time_end - time_start)


