class C:
    @property
    def field(self, value):
        return 'QQ'


    @field.setter
    def field(self, value):
        self._val = value

c = C()
c.field = 12456
