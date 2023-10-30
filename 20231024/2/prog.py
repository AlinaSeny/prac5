import itertools
import sys


def slide(seq, n):
    for i in range(len(seq)):
        yield from itertools.islice(seq, i, i + n)


exec(sys.stdin.read())
