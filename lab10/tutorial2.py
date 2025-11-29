import threading
import time

def zadanie(n):
    time.sleep(1)
    print(f"Start zadania {n}")
    time.sleep(1)
    print(f"Koniec zadania {n}")

watki = []

for i in range(5):
    t = threading.Thread(target=zadanie, args=(i,))
    watki.append(t)
    t.start()

for t in watki:
    t.join()

print("Wszystkie zadania zakończone.")
