import sys

with open(sys.argv[1], 'rt') as f:
    txt = f.read()

n = len(txt) // 3
p = txt[len(txt) // 3 - 1:].find('\n')
print(txt[:n + p])
