match input().split():
    case ['mov', r1, r2]:
        print([f"moving {r2} to {r1}"])
    case ['push', *var]:
        print(f'pushing {var}')
    case ['pop', *var]:
        print(f'poping {var}')
    case [cmd, r1]:
        print(f"making {cmd} with {r1}")
    case _:
        print(f'Parse error')
print()
