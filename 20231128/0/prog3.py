class Doubleton(type):
    _instance = [None, None]
    def __call__(cls, *args, **kw):
        res = cls._instance.pop(0)
        if res is None:
            res = super().__call__(*args, **kw)
        cls._instance.append(res)
        return cls._instance

class C(metaclass=Doubleton): pass
print(*(C() for i in range(7)), sep="\n")
