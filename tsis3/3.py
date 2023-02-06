def solve(numheads,numlegs):
    for i in range (numheads):
        if i*4 + (numheads -i) * 2 == numlegs:
            print(i, " ", numheads-i)
    
numheads = int(input())
numlegs = int(input())
solve(numheads,numlegs)
