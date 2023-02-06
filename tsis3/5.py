import itertools 
def permetation(x):
    d=itertools.permutations(x)
    for i in d:
        print(i)
     
x=input()
permetation(x)
