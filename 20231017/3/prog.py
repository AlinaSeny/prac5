n = int(input())
d = {}
while s := input().lower():
    r = ''
    for i in range(len(s)):
        if not s[i].isalpha():
            r += ' '
        else:
            r += s[i]
    r = r.split()
    for i in r:
        if i in d:
            d[i] += 1
        elif len(i) == n:
            d[i] = 1

if len(d):
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    maxx = sorted_d[0][1]
    res = []
    for i in sorted_d:
        if i[1] == maxx:
            res.append(i[0])
        else:
            break       
    if len(res) > 0:
        print(*sorted(res))
