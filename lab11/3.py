import time
import random

def stream():
    while True:
        yield random.randint(0, 1000)
        time.sleep(0.5)

def filter(stream, predicate):
    for x in stream:
        if predicate(x):
            yield x

def map(stream, fun):
    for x in stream:
        yield fun(x)

stream = stream()
filtered = filter(stream, lambda x: x > 500)
mapped = map(filtered, lambda x: str(x))

for x in mapped:
    print(x)