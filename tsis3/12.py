def histogram (list1):
    for i in list1:
        print(i*"*")
list1=list(map(int,input().split()))
histogram(list1)