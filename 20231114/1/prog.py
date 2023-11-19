def objcount(cls):
    class Decor(cls):
        counter = 0

        def __init__(self, *args, **kwargs):
            self.__class__.counter += 1
            if hasattr(super(), '__init__'):
                super().__init__(*args, **kwargs)

        def __del__(self):
            self.__class__.counter -= 1
            if hasattr(super(), '__del__'):
                super().__del__()

    return Decor

import sys
exec(sys.stdin.read())
