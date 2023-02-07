class Shape():
    def __init__(self):
        self.der=0
    def area(self):
        return self.der

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.der=self.length*self.width

x=Rectangle(2,4)
print(x.area())