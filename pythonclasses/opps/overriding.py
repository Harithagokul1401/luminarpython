class employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def printval(self):
        print(self.id)
        print(self.name)
        print(self.sal)
    

    def __str__(self):
        return self.name
    

obj=employee(1011,'ajay',25000)
obj1=employee(1012,'ajoy',75000)
obj2=employee(1021,'ayan',22000)

ls=[]
ls.append(obj)
ls.append(obj1)
ls.append(obj2)

for emp in ls:
    if(emp.sal>30000):
        print(emp)
    