def div(n):
    i=1
    while i < n:
        if i%3==0 and i%4==0:
            yield i
        i+=1
n= int(input())
d=div(n)
for b in d:
    print(b)