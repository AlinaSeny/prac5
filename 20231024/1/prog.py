def fib(m, n):
    if n > 0:
        count = 0
        prev = 0
        cur = 1
        while count < m:
            count += 1
            cur, prev = prev + cur, cur
        while count < m + n:
            yield cur
            count += 1
            cur, prev = prev + cur, cur

import sys
exec(sys.stdin.read())
