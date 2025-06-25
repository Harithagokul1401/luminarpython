import datetime
class bank:
# as the bank name is common to all and to save m/o we can declare bname as a static variable hr=ere
     bname = "SBI" # also class variable change will effect all
     def __init__(self,ano,name,bal):
         self.name=name
         self.ano=ano  # instance variable 1. Belong to each object (or instance) created from the class. 2.Defined inside methods, typically in __init__ using self.
         self.bal=bal
         #self.bname=bname

     def withdraw(self,ant):
         self.ant=ant  #local variable  once the method ends, it’s gone.
         balance= self.bal-ant
         if (balance<1000):
              print("\nSORRY!!!! you reached your minimum balance!!!\n")
         else:
               print("balance after withdraw : ",balance,"on",datetime.date.today())

     def deposit(self,dpt):
         self.dpt=dpt
         dbal=dpt+self.bal
         print("balance after deposit : ",dbal,"on",datetime.date.today())
     def enquiry(self):
         print("name :",self.name)
         print("bank name:",bank.bname) # yaha bank.banme hai kyuki bank ek class variable { hai ye koi function ke andhar nahi define hai } 
         print("account number:",self.ano)
         print("current balance:",self.bal)
         print("as of ",datetime.date.today())

obj=bank(234567,"arun viswanath",23000)
ans=int(input(f"welcome!!! {obj.name}!!\n choose your option\n1. withdraw\n2.deposit\n3.bank enquiry\n option:")) #f"'{self.title}' # obj.name calling using object
if (ans==1):
     w=int(input("enter the ampount to withdraw : "))
     obj.withdraw(w)
elif(ans==2):
     d=int(input("enter the ampount to deposit : "))
     obj.deposit(d)
else:
     obj.enquiry()

#Global Variables in Python
#✅ Defined outside of any class or function.
#✅ Accessible everywhere in the file (but not inside classes by default).