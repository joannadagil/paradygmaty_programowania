import threading

licznik = 0
def zwieksz():
    global licznik
    for _ in range(100000):
        licznik += 1

t1 = threading.Thread(target=zwieksz)
t2 = threading.Thread(target=zwieksz)
t1.start(); t2.start()
t1.join(); t2.join()

print(licznik) # wynik < 200000!


licznik2 = 0
lock = threading.Lock()
def zwieksz2():
    global licznik2
    for _ in range(100000):
        with lock:
            licznik2 += 1

t12 = threading.Thread(target=zwieksz2)
t22 = threading.Thread(target=zwieksz2)
t12.start(); t22.start()
t12.join(); t22.join()

print(licznik2) # 200000
