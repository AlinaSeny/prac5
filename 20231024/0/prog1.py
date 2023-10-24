def f(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / i ** 2
        yield s

print(list(f(5)))
