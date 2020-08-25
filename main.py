from celery import group, chain, chord
from proj.tasks import add, mul, xsum

if __name__ == '__main__':
    # (i + i) for i in range 100
    for i in range(100):
        result = add.delay(i, i)
        print(result.get(propagate=False))

    # signatures
    # (8 + 2)
    s1 = add.s(2)
    res = s1.delay(8)
    print(res.get())

    # groups
    # list of (10 + i) for i in range 10
    g = group(add.s(i) for i in range(10))
    print(g(10).get())

    # chains
    # (? + 4) * 8
    c = chain(add.s(4) | mul.s(8))
    print(c(4).get())

    # chord
    # sum of all i + i in range 10
    m = chord((add.s(i, i) for i in range(10)), xsum.s())().get()
    print(m)
