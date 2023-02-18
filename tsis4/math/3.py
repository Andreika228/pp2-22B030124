import math 
n=int(input("Numbers of sides "))
l=int(input("Length of a side "))
print("The area of the poligon is: ", round(n * (l**2)/4 * math.tan(math.pi/n)))