def Pareto(*x):
    t = list(x)
    res = []
    for i in range(len(t)):
        f = 1
        for j in range(len(t)):
            if i == j:
                continue
            if (t[i][0] < t[j][0] and t[i][1] <= t[j][1]) or (t[i][0] <= t[j][0] and t[i][1] < t[j][1]):
                f = 0
        if f:
            res.append(t[i])
    return tuple(res)

print(Pareto(*eval(input())))

