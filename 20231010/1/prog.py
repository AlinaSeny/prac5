from fractions import Fraction

l = input().split(",")
s, w = Fraction(l[0]), Fraction(l[1])
deg_a = int(l[2])
la = map(Fraction, l[3:3 + deg_a + 1])
deg_b = int(l[4 + deg_a])
lb = map(Fraction, l[5 + deg_a:])

suma = Fraction(0, 1)
sumb = Fraction(0, 1)

for i in la:
    suma += s**(deg_a) * i
    deg_a -= 1

for i in lb:
    sumb += s**(deg_b) * i
    deg_b -= 1

sumb *= w
if suma == sumb:
    print('True')
else:
    print('False')

