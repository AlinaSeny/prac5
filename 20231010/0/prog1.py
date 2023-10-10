from decimal import Decimal
from fractions import Fraction

def multiplier(x, y, Type):
    return Type(x) * Type(y)

print(multiplier(*eval(input())))

