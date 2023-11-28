from inspect import get_annotations


class A:
    param: int
    
    def __init__(self, new_param : int):
        if isinstance(new_param, get_annotations(A)['param']):
            self.param = new_param
        else:
            raise TypeError


print(get_annotations(A))
print(A(1))
