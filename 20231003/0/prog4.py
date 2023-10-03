def f(a, b):
    return lambda x: a*x + b
f2 = f(1, 2)
print(f2(3))

