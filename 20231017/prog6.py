from collections import Counter
import timeit

def ansc(s):
    Counter(s.split())

def ansd(s):
    s = s.split()
    d = {}
    for i in s:
        d[i] = d.setdefault(i, 0) + 1
    return d

print("counter time:", timeit.Timer('ansc("asdfghjklhgftfyhkjb")', globals=globals()).autorange())
print("dict time:", timeit.Timer('ansd("asdfghjklhgftfyhkjb")', globals=globals()).autorange())
