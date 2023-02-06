def rev(x):
    x = x.split()
    x.sort(reverse = True )
    x=" ".join(x)
    print(x)
    
x= input()
rev(x)
