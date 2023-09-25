def summ(t):
    res = 0
    while t:
        res += t % 10
        t //= 10
    return res

n = eval(input())
i = n
while i <= n + 2:
    j = n
    while j <= n + 2:
        if summ(i * j) == 6:
            s = ":=)"
        else:
            s = i * j
        print(i, "*", j, "=", s, end = " ")
        j += 1
    i += 1
    print()
