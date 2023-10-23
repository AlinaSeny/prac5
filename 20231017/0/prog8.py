import sys

f = sys.argv[1]

(a, b) = eval(" ".join(sys.argv[2:]))
print(eval(f, {"x": a, "y": b}))
print(eval(f, {"x": b, "y": a}))


