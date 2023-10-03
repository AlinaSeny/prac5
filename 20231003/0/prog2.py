def f(n):
    return 5*f(n-1) if n > 0 else 1
print(f(4))

