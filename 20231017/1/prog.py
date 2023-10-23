s = input().lower()
d = {}
prv = False
for i in s:
    if i.isalpha():
        if prv != False:
            d[prv + i] = 1
        prv = i
    else:
        prv = False
print(sum(d.values()))

