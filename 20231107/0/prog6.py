def div_ab(a, b):
    return a/b


inp = eval(input())
for i, j in inp:
    try:
        div_ab(i, j)
    except ZeroDivisionError:
        print("inf")
