class C:
    @property
    def age(self, value):
        return 'QQ'

    @age.setter
    def age(self, value):
        if value <= 128:
            self._val = value
        else:
            print("too old!")
            raise ValueError

    @age.getter
    def age(self):
        if self._val == 42:
            print("secret value!")
            return -1
        else:
            return self._val

c = C()
c.age = 4
print(c.age)
