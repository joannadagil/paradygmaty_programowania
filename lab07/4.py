def gen_fib():
    yield 0
    yield 1
    last = 1
    lastlast = 0
    while True:
        lastlast, last = last, last + lastlast
        yield last

def even(seq):
    for x in seq: 
        if x % 2 == 0: yield x

def sqrt(seq):
    for x in seq: yield x*x

if __name__ == "__main__":
    print("-------------- ZADANIE 4 --------------")
    gen = gen_fib()
    res = sqrt(even(gen))
    for _ in range(10):
        print(next(res), end=" ")
    print()