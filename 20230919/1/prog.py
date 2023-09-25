t = eval(input())
a = "+"
b = "-"
c = "+"

if t % 50 != 0:
    a = "-"
    b = "+"
if t % 8 != 0:
    c = "-"
print("A", a, "B", b, "C", c)
