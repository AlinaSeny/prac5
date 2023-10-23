from math import *

df = {}
cf = 1
cs = 0
while s := input():
    cs += 1
    if s[0] == ':':
        cf += 1
        s = s[1:].split()
        expr = "lambda " + ','.join(s[1:-1]) + ":" + s[-1]
        df[s[0]] = (eval(expr), len(s[1:-1]))
    else:

        if s.split()[0] == "quit":
            s = s.split()
            exec(f"print({' '.join(s[1:])}.format(cf, cs))")
            break
        else:
            args = []
            if ' ' not in s:
                func = s
            else:
                func = s[:s.index(' ')]
                if df[func][1] == 1:
                    c = '"'
                    if "'" in s:
                        c = "'"
                    s = s.split(c)
                    args.append(s[1])
                else:
                    args = []
                    s = s.split()
                    for arg in s[1:]:
                        args.append(eval(arg))
            if len(args) > 0:
                print(df[func][0](*args))
            else:
                print(df[func][0]())
