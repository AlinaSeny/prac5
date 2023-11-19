class Num:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        value = getattr(instance, self.private_name, 0)
        return value

    def __set__(self, instance, value):
        if hasattr(value, "real"):
            setattr(instance, self.private_name, value)
        elif hasattr(value, "__len__"):
            setattr(instance, self.private_name, len(value))


import sys
exec(sys.stdin.read())
