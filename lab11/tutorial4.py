import time
import random

def strumien_temperatur():
    while True:
        yield random.randint(0, 150)
        time.sleep(0.5)

def filtruj(stream, predykat):
    for x in stream:
        if predykat(x):
            yield x

def mapuj(stream, funkcja):
    for x in stream:
        yield funkcja(x)

strumien = strumien_temperatur()
strumien_przefiltrowany = filtruj(strumien, lambda x: x > 50)
strumien_przeksztalcony = mapuj(strumien_przefiltrowany, lambda x: x * 1.8 + 32)

for temp in strumien_przeksztalcony:
    print(f"Temperatura w °F: {temp}")