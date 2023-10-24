import itertools
import random

def repeater(seq, n):
    for el in seq:
        yield from itertools.repeat(el, n)

print(list(repeater("QWER", 5)))

