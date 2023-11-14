class Desc:

    def __get__(self, obj, cls):
        print("GET", obj, cls)
        return obj._val

    def __set__(self, obj, val):
        print("SET", obj, val)
        obj._val = val
'''
    def __delete__(self, obj):
        print(f"Delete from {repr(obj)}")
        obj._value = None
'''


class C:
    data = Desc()

    def __str__(self):
        return f'<{self.data}'

c = C()

print(dir(c))

c.data = 5
print(c.data)
