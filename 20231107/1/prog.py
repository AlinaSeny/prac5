import collections


class DivStr(collections.UserString):
    def __init__(self, seq=''):
        super().__init__(seq)

    def __floordiv__(self, n):
        k = len(self) // n
        res = []
        for i in range(n):
            res.append(self[i * k:k * (i + 1)])
        return iter(res)

    def __mod__(self, n):
        k = len(self) % n
        if k != 0:
            return self[-k:]
        else:
            return DivStr()


import sys
exec(sys.stdin.read())

