import string


class Alpha:
    __slots__ = list(string.ascii_lowercase)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        s = [f"{slot}: {getattr(self, slot)}"
             for slot in self.__slots__ if hasattr(self, slot)]
        return ", ".join(s)


class AlphaQ:

    def __init__(self, **kwargs):
        lowercase = set(string.ascii_lowercase)
        for key, value in kwargs.items():
            if key not in lowercase:
                raise AttributeError(f"'{self.__class__.__name__}' object has not attribute '{key}'")
            self.__dict__[key] = value

    def __setattr__(self, key, value):
        if key not in set(string.ascii_lowercase):
            raise AttributeError(f"'{self.__class__.__name__}' object has not attribute '{key}'")
        self.__dict__[key] = value

    def __str__(self):
        s = [f"{key}: {self.__dict__[key]}" for key in sorted(self.__dict__)]
        return ", ".join(s)


import sys
exec(sys.stdin.read())
