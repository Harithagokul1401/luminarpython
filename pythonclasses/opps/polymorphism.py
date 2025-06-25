# polymorphism = many forms 
# method overloading
# method overriding
# operator overloading

# method overloading : same method name with diff arguments
class math:
    def add(self):
        n=10
        m=20
        print(n+m)
    def add(self,n):
        m=20
        print(n+m)
    def add(self,n,m):
        print(n+m)

m=math()
m.add(10,20) # third vala add hoga run
m.add(10)  # shows error aspython dontn support this 
            #it ask for another argument
            #recent vala method hi work hoga


# method overriding
# example  1
class parent:
    def phone(self):
        print("samsung galaxy a6")

class child(parent):
    def phone(self):
        print("iphone")

c=child()
c.phone() #child vala phone hoga work agar parent vala chahiye to parent ka alag obj create karna hoga

#ex 2
class parent:
    def property(self):
        print("i am parent of")
    def marriage(self):
        print("i am adopted")

class child(parent):
    def marriage(self):
        print("shivani")

c=child()
c.property()
c.marriage() # yaha c obj ko adopt nahi hona so we overwrite marriage in child
 

3.

class employee:
    def __init__(self,name,sal):
        self.id=id
        self.name=name 
        self.sal= sal

    def private(self):
        print(self.id)
        print(self.name)
        print(self.sal)

obj=employee(1011,'ajay',25000)
print(obj)  # output will be a hexadecimal value it is m/o location of object

#when object is called def__str__(self) call hota hai 