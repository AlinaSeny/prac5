import itertools
import random

def ffn(n, seq):
    yield from itertools.filterfalse(lambda x: x%n, seq)

ffn(5, (random.range(50) for i in range(100)))

