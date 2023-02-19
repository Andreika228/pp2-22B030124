def gen (n):
    while n > -1:
        yield n
        n-=1
n= int(input())
g=gen(n)
for i in g:
    print(i)