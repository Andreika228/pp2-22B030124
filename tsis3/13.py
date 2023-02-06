import random
def num (name):
    print("Well",name,"I am thinking of a number between 1 and 20")
    x=random.randint(1,20)
    for i in range(x):
        print("Take a guess.")
        a=int(input())
        if a>x:
            print("Your guess is too high")
        elif a<x:
            print("Your guess is too low")
        else:
            print("Good job, ",name, " You guessed my number in ",i+1, " guesses!")
            break 
print("Hello! What is your name?")
name=input()
num(name)
