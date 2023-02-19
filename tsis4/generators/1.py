def squares (n):
    i=0
    while i < n:
        yield i*i
        i+=1

n=int(input())
sq = squares(n)
for b in sq:
    print(b)