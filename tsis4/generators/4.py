def squares (a,b):
    while a<b:
        yield a**2
        a+=1
a= int(input())
b= int(input())
sq= squares(a,b)
for i in sq:
    print(i)