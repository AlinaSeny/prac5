a, b, c = input().split()

while s := input():
    match s:
        case [a, *args] if 'yes' in args:
            print('case 1')
        case [b]:
            print('case 2')
        case [c, *var, b]:
            print('case 3')
        case _:
            print("'_'")
