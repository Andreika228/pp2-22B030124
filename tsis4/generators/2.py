def even (n):
   i=0
   while i < n:
       if i%2==0:
           yield i
       i+=1
        
n=int (input())
ev= even(n)
for b in ev:
    print(b,end=", ")