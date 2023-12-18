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


import sys
exec(sys.stdin.read())
