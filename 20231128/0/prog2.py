class final(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) > 1:
            raise TypeError(f"More than one parent")
        return super().__new__(metacls, name, parents, namespace)
class E(metaclass=final): pass
