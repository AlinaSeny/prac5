sum = 0
while t := input():
    if int(t) <= 0:
        print(t)
        break
    else:
        sum += int(t)
        if sum > 21:
            print(sum)
            break