db=[["Rishabh",1234,3456,1000],["Sid",1222,3656,1600],["Mahi",1284,3056,1070],["Kashish",1034,3416,1400]]
class Account:
   
    def __init__(self,balance=0):
        self.balance=balance
        
    def func(self,name):
        self.name=name
        e=input("enter 'd' to deposit"+"\n"+"enter 'w' to withdrawl"+"\n"+"enter 'c'to check balance"+"\n"+"To change your current pin press 'cp'"+"\n"+"To exit press e"+"\n")
        if e=='d':
            damount=int(input("Enter the amount you want to deposit"))
            d1.deposit(damount,name)
            another=input("do you want another transaction enter Y or N")
            if another=='Y':
                d1.func(name)
            elif another=='N':
                d1.main()
        elif e=='w':
            wamount=int(input("Enter the amount you want to withdraw"))
            d1.withdrawl(wamount)
            another=input("do you want another transaction")
            if another=='Y':
                d1.func(name)
            elif another=='N':
                d1.main()
        elif e=='c':
            print("your balance is")
            print(d1.checkBalance())
            another=input("do you want another transaction")
            if another=='Y':
                d1.func(name)
            elif another=='N':
                d1.main()
        elif e=='cp':
            d1.changePassword(self.pin)
            another=input("do you want another transaction")
            if another=='Y':
                d1.func(name)
            elif another=='N':
                d1.main()
        elif e=='e':
            d1.main()
    
    def deposit(self,credit,uname):
        self.uname=uname
        for i in db:
            if uname==i[0]:
                self.balance+=credit
                i[3]+=self.balance
                print("Your new updated balance is:" ,i[3])
                print(db)
    
        
    def withdrawl(self,debit):
        if self.balance>=debit:
            self.balance-=debit
            print("Your updated balance is:" ,self.balance)
        else:
            print("Insufficients Funds")
            print("your balance" ,self.balance) 
    
    def checkBalance(self):
        mybalance=self.balance
        print(mybalance)
        return " "
    
    def transaction(self,uname,pin):
        self.pin=pin
        self.uname=uname
        for i in db:
            if uname==i[0]:
                if pin==i[1]:
                    d1.func(uname)
                else:
                    print("wrong pin")
                    break
                    d1.main()
    def changePassword(self,pin):
        np=int(input("Enter your new pin"))
        self.pin=np
        print("Your new pin is",self.pin)
        for i in db:
            if i[0]==self.uname:
                i[1]=self.pin
                print("your new pin is",self.pin)
                print(db)
        
        
    
    def main(self):
        n=input("enter your name"+" ")
        p=int(input("Enter the pin"+" "))
        d1.transaction(n,p)
width=50
print("WELCOME TO SWIZZ BANK".center(width,'*'))
d1=Account()
d1.main()        


