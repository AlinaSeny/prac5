import pickle

class SerCls:
    lst = []
    dct = {}
    numpyst = 1
    st = ''
    
    def __init__(self):
        self.lst = [1]
        self.dct['a'] = 2
        self.nem  = 2
        self.st = 'QWER'
        
    
ser = SerCls()
s = pickle.dumps(ser)
print(s)
del ser
print(s)
ser = pickle.load(s)
print(ser)
