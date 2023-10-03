def h(f, g):
    def m(x):
    	return f(x) + g(x)
    return m
print(h(bin, hex)(3))

