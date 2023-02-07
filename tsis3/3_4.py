class Point:
    def __init__(self,xcordinate,ycordinate):
        self.xcordinate=xcordinate
        self.ycordinate=ycordinate
    def show(self):
        print(f"Coordinates of point ({self.xcordinate};{self.ycordinate})")
    def move(self):
        print("Write a new coordinates for point: ")
        self.xcordinate=int(input())
        self.ycordinate=int(input())
    def dist(self,xcord2,ycord2):
        print(f"Distance between ({self.xcordinate};{self.ycordinate}) and ({xcord2};{ycord2}): ", round(((self.xcordinate-xcord2)**2+(self.ycordinate-ycord2)**2)**(1/2),3),sep=' ')

x=Point(1,2)
x.show()
x.move()
x.show()
x.dist(3,4)