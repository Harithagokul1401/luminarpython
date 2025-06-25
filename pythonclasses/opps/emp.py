# to take the input from file and to assihn them to object of class

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


for emp in emplst:# obj is called as emp and the ouput is name as str def consist of name
    print(emp)
    