def agent (list1):
    for i in range(len(list1)-1):
        cnt = 0
        if list1[i]==0 and list1[i+1]==0 and list1[i+2]==7:
            cnt+=1
            print("True")
            break
    if cnt==0:
        print("False")    
list1=list(map(int,input().split()))
agent(list1)
