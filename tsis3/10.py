def eniq (list1,list2):
    for i in list1:
        if not i in list2:
            list2.append(i)
    print (list2)        
            
list1=list(map(int,input().split()))
list2=[]
eniq(list1,list2)