def calc(n):
    up=0
    for i in n:
        if i>="A" and i<= "Z":
            up+=1 
    return up
def calc1(n):
    low=0
    for i in n:
        if i>="a" and i<="z":
            low+=1
    return low
            
n=input()
print("Number of uppercase: ", calc(n), "Number of lowercase: " ,calc1(n))