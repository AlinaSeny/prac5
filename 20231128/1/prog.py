def decor(name, func):
    def new_func(self, *args, **kwargs):
        print(name + ":", args, kwargs)
        return func(self, *args, **kwargs)
    return new_func


class dump(type):
    def __new__(cls, name, parents, attrs, **kwargs):
        for i in attrs:
            if callable(attrs[i]):
                attrs[i] = decor(i, attrs[i])
        return super().__new__(cls, name, parents, attrs)


class C(metaclass=dump):
    def __init__(self, val):
        self.val = val

    def add(self, other, another=None):
        return self.val + other + (another or self.val)

c = C(10)
print(c.add(9))
print(c.add(9, another=10))
