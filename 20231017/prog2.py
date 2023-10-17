l1 = ["A", "E", "I", "O", "U", "Y"]
l2 = ["B", "C", "D","F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
d1 = {i.lower() : 0 for i in l1}
d2 = {i.lower() : 0 for i in l2}

s = input()

for i in s:
    if i in d1:
        d1[i] = 1
    elif i in d2:
        d2[i] = 1

print("гласные:", sum(d1.values()))
print("согласные:", sum(d2.values()))
