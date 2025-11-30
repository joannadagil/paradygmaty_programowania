import time
import random

def strumien_temperatur():
    while True:
        yield random.randint(0, 150)
        time.sleep(0.5)

def monitoruj_strumien(stream):
    for temp in stream:
        print(f"Temperatura: {temp}")
        if temp > 100:
            print("⚠ Przekroczono próg temperatury!")

monitoruj_strumien(strumien_temperatur())
