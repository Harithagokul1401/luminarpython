def ad(a,b):
    s=a+b
    print("your ans :",s)

def sub(a,b):
    d = a-b
    print("your ans :",d)

def mul(a,b):
    m=a*b
    print("your ans :",m)

def div(a,b):
    d=a/b
    print("your ans :",d)

x= int(input("enter the first value(x>y) :"))
y = int(input(" enter the second value(x>y):"))
op = int(input("enter your option \n 1. add\n 2.subtract\n 3.multiply\n 4.division\n option number :"))
if(op==1):
    ad(x,y)
elif(op==2):
    sub(x,y)
elif(op==3):
    mul(x,y)
else:
    div(x,y)