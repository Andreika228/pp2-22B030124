class Account:
    def __init__(self,owner,balance): 
        self.owner=owner
        self.balance=balance
        self.dep=0
    def withdraw(self,summa):
        if summa>self.balance:
            print(self.owner, "You have too little money")
        else:
            self.balance=self.balance-summa
            print(self.owner, "your balance is:",self.balance)
    def deposit(self, summa):
        if summa>self.balance:
            print(self.owner, "You have too little money")
        else: 
            self.balance=self.balance-summa
            self.dep=self.dep+summa
            print( "Your deposit replenished on",summa,"\n",self.owner, "your balance is:", self.balance,)

x=Account("Andrey",5000)
x.withdraw(2000)
x.deposit(1000)
x.withdraw(10000)
x.deposit(20000)

