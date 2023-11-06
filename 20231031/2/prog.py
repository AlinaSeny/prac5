from __future__ import annotations

import math
import itertools


def vect_prods(x, y, x0, y0, x1, y1, x2, y2):
    res = ((x0 - x) * (y1 - y) - (x1 - x) * (y0 - y),
           (x1 - x) * (y2 - y) - (x2 - x) * (y1 - y),
           (x2 - x) * (y0 - y) - (x0 - x) * (y2 - y))
    return res


# thanks to: https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
def do_intersect(a, b, c, d):
    COLLINEAR = 0
    CLOCKWISE = 1
    COUNTERCLOCKWISE = -1

    def orientation(a, b, c):
        val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
        if val > 0:
            return CLOCKWISE
        elif val < 0:
            return COUNTERCLOCKWISE
        else:
            return COLLINEAR

    def between(a, c, b):
        if min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and \
                min(a[1], b[1]) <= c[1] <= max(a[1], b[1]):
            return True
        return False

    o1 = orientation(a, b, c)
    o2 = orientation(a, b, d)
    o3 = orientation(c, d, a)
    o4 = orientation(c, d, b)

    if (o1 != o2) and (o3 != o4):
        return True

    if (o1 == COLLINEAR) and between(a, c, b) or \
            (o2 == COLLINEAR) and between(a, d, b) or \
            (o3 == COLLINEAR) and between(c, a, d) or \
            (o4 == COLLINEAR) and between(c, b, d):
        return True
    return False


class Triangle:

    def __init__(self, c1, c2, c3):
        self.c1 = tuple(c1)
        self.c2 = tuple(c2)
        self.c3 = tuple(c3)

        self.a = ((self.c1[0] - self.c2[0]) ** 2 + (self.c1[1] - self.c2[1]) ** 2) ** (1 / 2)
        self.b = ((self.c1[0] - self.c3[0]) ** 2 + (self.c1[1] - self.c3[1]) ** 2) ** (1 / 2)
        self.c = ((self.c2[0] - self.c3[0]) ** 2 + (self.c2[1] - self.c3[1]) ** 2) ** (1 / 2)

    def __abs__(self):
        if max(self.a, self.b, self.c) >= self.a + self.b + self.c - max(self.a, self.b, self.c):
            return 0

        d11, d12 = self.c1[0] - self.c3[0], self.c1[1] - self.c3[1]
        d21, d22 = self.c2[0] - self.c3[0], self.c2[1] - self.c3[1]
        return abs(d11 * d22 - d12 * d21) / 2

    def __bool__(self):
        return abs(self) != 0

    def __lt__(self, other: Triangle):
        return abs(self) < abs(other)

    def __contains__(self, other: Triangle):
        if not other:
            return True
        if not self:
            return False

        for point in [other.c1, other.c2, other.c3]:
            prods = vect_prods(point[0], point[1],
                               self.c1[0], self.c1[1],
                               self.c2[0], self.c2[1],
                               self.c3[0], self.c3[1])
            if any(p == 0 for p in prods):
                continue

            prods = list(map(lambda x: math.copysign(1.0, x), prods))
            if any(p != prods[0] for p in prods):
                return False

        return True

    def __and__(self, other: Triangle):
        if not self or not other:
            return False

        for a, b in itertools.combinations([self.c1, self.c2, self.c3], 2):
            for c, d in itertools.combinations([other.c1, other.c2, other.c3], 2):
                if do_intersect(a, b, c, d):
                    return True
        return False



