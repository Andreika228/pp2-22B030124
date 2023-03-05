def ret(list1):
    mult=1
    for i in list1:
        mult*=i
    return mult    
list1=[i for i in range(1,5)]
print(ret(list1))
print (list1)