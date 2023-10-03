def addres(n):
    res = []
    for i in range(n):
        def addres(x):
            return x + i
        res.append(adder)
    return res

