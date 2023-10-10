from decimal import Decimal, getcontext

def esum(N, one):
    tp = type(one)
    sum = tp('1')
    fr = tp('1')
    for i in range(1, N+1):
        fr *= tp(f"{i+1}")
        sum += tp(1)/fr
    return sum + 1

print(esum(5, Decimal(1)))
