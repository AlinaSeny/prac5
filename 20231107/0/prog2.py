class A:
    def __init__(self, var):
        self.var = var

    def __add__(self, other):
        return self.__class__(self.var + other)

a = A(1)
print(a)
print(a.var)
print((a + 1).var)

class B(A):
    def __str__(self):
        return (f"<{self.var}>")

a = B(12)
print(a)
