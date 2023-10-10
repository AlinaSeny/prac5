from math import sin

def scale(a, b, A, B, x):
    for i in range(a, b):
        return (x-a)*(B-A) / (b-a) + A


W, H = 60, 20
lst = [[' '] * W for i in range(H)]
A, B = -5, 5
for i in range(W):
    x = scale(0, W-1, -5, 5, i)
    y = sin(x)
    w = int(scale(-1, 1, H-1, 0, y))
    lst[w][i] = "*"

print("\n".join("".join(s) for s in lst))
