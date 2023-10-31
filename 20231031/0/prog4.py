class Rectangle:
    rectcnt = 0

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        Rectangle.rectcnt += 1
        setattr(self, f"rect_{Rectangle.rectcnt}", 0)

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1})"


    def __lt__(self, a):
        return (self.x2 - self.x1) * (self.y2 - self.y1) < (a.x2 - a.x1) * (a.y2 - a.y1)


    def __eq__(self, a):
        return (self.x2 - self.x1) * (self.y2 - self.y1) == (a.x2 - a.x1) * (a.y2 - a.y1)


a = Rectangle(1, 2, 3, 4)
b = Rectangle(1, 2, 3, 4)
print(a < b)
print(a == b)
