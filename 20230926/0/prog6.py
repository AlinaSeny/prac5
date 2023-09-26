import pprint
a = []
while lst := input():
    a.append(eval(lst))
b = len(a)
if all([len(el) == b for el in a]):
    for i in range(b):
        for j in range(i + 1, b):
            a[i][j], a[j][i] = a[j][i], a[i][j]
for i in a:
    print(*i)
