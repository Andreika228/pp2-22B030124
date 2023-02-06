def ispalindrom (x):
    if str(x) == str(x)[::-1] :
        print("palindrome")
    else:
        print("not Palindrome")
x=input()
ispalindrom(x)