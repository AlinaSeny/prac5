from functools import wraps


def debug(fun):
    @wraps(fun)
    def wrapper(*args):
        for arg in args:
            if type(arg) != int:
                raise TypeError
        print("<", *args)
        res = fun(*args)
        print(">", res)
        return res
    return wrapper


@debug
def mult(a, b):
    """This is mult"""
    return a * b


print(mult(2, 'f'))
