s = input()
s = s.split()
d = {}
for i in s:
    d[i] = d.setdefault(i, 0) + 1
print(d)
