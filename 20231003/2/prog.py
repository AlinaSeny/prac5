def sub(x, y):
    if isinstance(x, tuple) or isinstance(x, list):
        res = []
        for i in x:
            if i not in y:
                res.append(i)
        return type(x)(res)
    return x - y

print(sub(*eval(input())))