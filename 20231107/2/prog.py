class InvalidInput(Exception):
    pass


class BadTriangle(Exception):
    pass


def triangleSquare(s):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(s)
    except Exception:
        raise InvalidInput
    try:
        assert type(x1) == float or type(x1) == int
        assert type(x2) == float or type(x2) == int
        assert type(x3) == float or type(x3) == int
        assert type(y1) == float or type(y1) == int
        assert type(y2) == float or type(y2) == int
        assert type(y3) == float or type(y3) == int
    except Exception:
        raise BadTriangle
    a = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** (1 / 2)
    b = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** (1 / 2)
    c = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
    if max(a, b, c) >= a + b + c - max(a, b, c):
        raise BadTriangle
    sq = 1/2 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    if sq == 0:
        raise BadTriangle
    return sq


while True:
    try:
        res = triangleSquare(input())
    except InvalidInput:
        print('Invalid input')
    except BadTriangle:
        print('Not a triangle')
    else:
        print(f'{res:.2f}')
        break


