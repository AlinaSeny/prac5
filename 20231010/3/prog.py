from math import ceil

s = input()
m = len(s)
n = 1
dot_c, tilde_c = 0, 0
while s := input():
    dot_c += s.count(".")
    tilde_c += s.count("~")
    n += 1

vol = dot_c + tilde_c

tilde_m = ceil(tilde_c / (n - 2))
dot_m = m - 2 - tilde_m

print("#"*n)
for i in range(dot_m):
    print('#' + '.' * (n-2) + '#')

for i in range(tilde_m):
    print('#' + '~' * (n-2) + '#')
print("#"*n)

div = max(dot_c, tilde_c)
end = len(str(div)) + 1 + len(str(vol))
print(f"{round(20 * dot_c / div) * '.':<20}", f"{str(dot_c) + '/' + str(vol):>{end}}")
print(f"{round(20 * tilde_c / div ) * '~':<20}", f"{str(tilde_c) + '/' + str(vol):>{end}}")

