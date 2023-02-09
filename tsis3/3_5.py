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
            print(f"{self.owner}, your balance is: {self.balance}")
    def deposit(self, howmuch):
        if howmuch>self.balance:
            print(f"{self.owner}, You have too little money")
        else: 
            self.balance=self.balance-howmuch
            self.dep=self.dep+howmuch
            print(f"Your deposit replenished on {howmuch}\n{self.owner}, your balance is: {self.balance}")

x=Account("Andrey",5000)
x.withdraw(2000)
x.deposit(1000)
x.withdraw(10000)
x.deposit(20000)

