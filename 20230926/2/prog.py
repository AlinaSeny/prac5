lst = [int(i) for i in input().split(",")]
for i in range(0, len(lst)):
    for j in range(0, len(lst) - i - 1):
        if ((lst[j + 1])**2)%100 < ((lst[j])**2)%100:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)

