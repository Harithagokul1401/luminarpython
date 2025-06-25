class employee:
    def __init__(self,id,name,desig,sal):
        self.id=id
        self.name=name
        self.desig=desig
        self.sal=sal

    def printemp(self):
        print("\nname : ",self.name)
        print("desig : ",self.desig)

    def __str__(self):  # by default runs whena object is called
        return self.name
emplst=[] # to store value of each object stored in ls

f=open("opps//empdetail.txt","r")
for data in f:
    #print(data)
    ls=data.rstrip("\n").split(",")
    #print (ls)
    id= ls[0]
    name=ls[1]
    dsg=ls[2]
    sal=ls[3]
    obj=employee(id,name,dsg,sal)
    obj.printemp()
    emplst.append(obj)  # lst me objeect ko add kiya




#to all1. to print every name in uppercase
#2, print employee name with sal >25000
# 3, to provide increment5000 


# 1️⃣ Print every name in uppercase
def upper_case(emp):
    print(emp.name.upper())

print("\n--- Names in Uppercase ---")
list(map(upper_case, emplst))

# 2️⃣ Print employees with salary > 25000
print("\n--- Employees with Salary > 25000 ---")
high_sal_emps = filter(lambda emp: int(emp.sal) > 25000, emplst)
for emp in high_sal_emps:
    print(emp)

# 3️⃣ Provide increment of 5000
print("\n--- Salaries after Increment of 5000 ---")
new_salaries = list(map(lambda emp: int(emp.sal )+ 5000, emplst))
print(new_salaries)
