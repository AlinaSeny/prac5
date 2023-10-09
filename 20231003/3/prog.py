from math import *

def Calc(s, t, u):
    def res(a):
        y = lambda x: eval(t)
        y = y(a)
        x = lambda x: eval(s)
        x = x(a)
        return eval(u)
    return res


f = Calc(*eval(input()))
print(f(eval(input())))
