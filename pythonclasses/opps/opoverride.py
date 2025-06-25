class book :
    def __init__(self,page):
        self.page=page

    def __str__(self):  # to print ..when we use print __str__ class is called
        return str(self.page)
    
    def __add__(self,other):
        return book(self.page+other.page)   # return int vales
    
ob=book(100)
ob2=book(200)
print(ob+ob2)  #error as ob is type of book neither int or str

# to overright plus sign in 10th line we use add function
ob3=book(300)
print(ob+ob2+ob3)  # error 
# as ob+ob1 add will be caleed and return int but at next step 300+ob2 is erroe as int+book type is erroe
# as str function return int make it book type .. so thats why str vala function me return book type kita hai
# now ob+ob1 return book and ob3 isalso book so no error