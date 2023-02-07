class Shape():
    def __init__(self):
        self.ret=0
    def area(self):
        return self.ret

class Square(Shape):
    def __init__(self,length):
        self.length=length
        self.ret=self.length**2

x=Shape()
print(x.area())
y=Square(2)
print(y.area())
