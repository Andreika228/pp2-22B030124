class Account:
    def __init__(self,owner,balance): 
        self.owner=owner
        self.balance=balance
        self.dep=0
    def withdraw(self,howmuch):
        if howmuch>self.balance:
            print(f"{self.owner}, You have too little money")
        else:
            self.balance=self.balance-howmuch
            print(f"{self.owner}, your certain balance: {self.balance}")
    def deposit(self, howmuch):
        if howmuch>self.balance:
            print(f"{self.owner}, You have too little money")
        else: 
            self.balance=self.balance-howmuch
            self.dep=self.dep+howmuch
            print(f"Your deposit replenished on {howmuch}\n{self.owner}, your certain balance: {self.balance}")

print("Hello,lets create a new bank account")
x=input("Enter your name: ")
y=int(input("Enter your balance: "))
acc=Account(x,y)
while True:
    c=input("What do you want to do: (Balance) (Deposit) (Withdraw) (Exit): ")
    if c=='Balance':
        print(f"{acc.owner}, your certain balance: {acc.balance}")
    elif c=='Deposit':
        d=int(input(f"{acc.owner}, how much do you want to top up your deposit? "))
        acc.deposit(d)
    elif c=='Withdraw':
        d=int(input(f"{acc.owner}, how much do you want to withdraw? "))
        acc.withdraw(d)
    elif c=='Exit':
        print(f'{acc.owner}, we are still waiting for you, goodbye')
        break
    else:
        print('''You have only 3 options:
(Deposit)
(Withdraw)
(Exit)''')