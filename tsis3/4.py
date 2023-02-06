def filter_prime(list1):
    for el in list1:
        if isprime(el) == True:
            continue
        else:
            list1.remove(el)
    for i in list1:
        print(i,end=" ")
def isprime (el):
    cnt=0
    for i in range(1,el):
        if el%i==0 :
            cnt+=1
    if cnt<=2:
        return True
    else:
        return False
            
               
list1 = list(map(int,input().split()))
filter_prime(list1)
