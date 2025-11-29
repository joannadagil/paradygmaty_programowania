import threading

def przetwarzaj_fragment(dane, start, end):
    fragment = dane[start:end]
    wynik = sum(fragment)
    print(f"Suma fragmentu {start}-{end}: {wynik}")

dane = list(range(1_000_000))
n = len(dane)//4
watki = []

for i in range(4):
    t = threading.Thread(target=przetwarzaj_fragment, args=(dane, i*n, (i+1)*n))
    watki.append(t)
    t.start()

for t in watki:
    t.join()
