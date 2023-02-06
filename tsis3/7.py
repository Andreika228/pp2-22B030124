def fod (list1):
    cnt =0
    for i in range(len(list1)-1):
        if list1[i]==list1[i+1]:
            cnt+=1
            print("True")
            break
    if cnt==0:
        print("False")
                

        
list1=list(map(int,input().split()))
fod(list1)