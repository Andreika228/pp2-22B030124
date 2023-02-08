class Account:
    def __init__(self,user,balance): 
        self.user=user
        self.balance=balance
        self.dep=0
    def withdraw(self,howmuch):
        if howmuch>self.balance:
            print(f"{self.user}, You have too little money")
        else:
            self.balance=self.balance-howmuch
            print(f"{self.user}, your balance is: {self.balance}")
    def deposit(self, howmuch):
        if howmuch>self.balance:
            print(f"{self.user}, You have too little money")
        else: 
            self.balance=self.balance-howmuch
            self.dep=self.dep+howmuch
            print(f"Your deposit replenished on {howmuch}\n{self.user}, your balance is: {self.balance}")

print("Hello,lets create a bank account")
x=input("Enter your name: ")
y=int(input("Enter your balance: "))
acc=Account(x,y)
m= True
while m:
    v=input("What do you want to do: (Deposit) (Balance) (Withdraw) (Exit): ")
    if v=='Balance':
        print(f"{acc.user}, your balance is: {acc.balance}")
    elif v=='Deposit':
        d=int(input(f"{acc.user}, how much do you want to top up your deposit? "))
        acc.deposit(d)
    elif v=='Withdraw':
        d=int(input(f"{acc.user}, how much do you want to withdraw? "))
        acc.withdraw(d)
    elif v=='Exit':
        print(f'{acc.user}, Thank you for using our banking system, come again, goodbye')
        m=False
    else:
        print('''You have only 3 options:
(Deposit)
(Withdraw)
(Exit)''')