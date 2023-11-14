def repeat(n):
    def repeater(fun):
        def newfun(*args):
            for arg in args:
                if not isinstance(arg, n):
                    raise TypeError
            return True
        return newfun
    return repeater


@repeat(int)
def mult(a, b):
    return a * b

print(mult(8.0, 9))
