from itertools import dropwhile, count

def f():
    s = 0
    for i in count(1):
        s += 1 / i ** 2
        yield s

ite = dropwhile(lambda x: x < 1.6, f())
print(*list(next(ite) for i in range(10)), sep = "\n")
