class dert():
    '''ввести и вывести стринг значение'''
    def __init__(self):
        self.somestring=''
    def getString(self):
        self.somestring=input()
    def printString(self):
        print(self.somestring.upper(), end='')

x=dert()
x.getString()
x.printString()
