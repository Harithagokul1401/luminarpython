import functools 
lst=[10,20,3,40]
total= functools.reduce(lambda num1,num2:num1+num2,lst)
print(total)            # 10,20:10+20=30
                        #30+3=33
                        #33+40=73

# reduce  --> iterables se ek single value milega
#reduce() is a function that reduces a list (or any iterable) into a single value
#  by applying a function cumulatively to the items.

#✅ When to use reduce():
# When you want to accumulate values into one result.

# Examples: sum, product, finding max/min, combining strings, etc.

# ✅ Important:
# You can often use sum(), max(), min() directly.

# reduce() is powerful for custom accumulation logic.

# to find max value
maxval=functools.reduce(lambda n1,n2:n1>n2,lst)
print(maxval)

# simplyget o/p by print(max(lst))
# but in prg ;ile employee vala list me object hai..max function sirf int e kaam karta hai
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
    emplst.append(obj) 

# to print max sal
salary=list(map(lambda obj:obj.sal,emplst)) #this step is becoz emp me object store hai and usko list me convert kiya hai
print(salary)
maxsal=functools.reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,salary)
print(maxsal)                                                        
#  from functools import * use at top
# u dont have to use functool.reduce at every line ,..using line 62 ...simply use reduce 

# to print name of max sal
maxsalemp=list(filter(lambda emp:emp.sal==maxsal,emplst))
for emp in maxsalemp:
    print(emp)