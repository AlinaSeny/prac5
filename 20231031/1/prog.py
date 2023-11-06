class Omnibus:
    attrs = {}

    def __init__(self):
        self.__dict__['attrs'] = []

    def __setattr__(self, key, value):
        if key[0] != '_':
            if key not in self.__class__.attrs:
                self.__class__.attrs[key] = 1
                self.__dict__['attrs'].append(key)
            elif key not in self.__dict__['attrs']:
                self.__class__.attrs[key] += 1
                self.__dict__['attrs'].append(key)

    def __getattr__(self, item):
        if item[0] == '_':
            return None
        else:
            if item in self.__class__.attrs:
                return self.__class__.attrs[item]
            else:
                return 0

    def __delattr__(self, item):
        if item in self.__dict__['attrs']:
            self.__class__.attrs[item] -= 1
            self.__dict__['attrs'].remove(item)


import sys
exec(sys.stdin.read())
