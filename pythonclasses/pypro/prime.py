n = int(input("enter ypou number :"))
i =1
for i in range (1,n-1,i+1):
    if(n%i==0):
        flag =0
    else:
        flag +=1
if(flag>0): print("prime")
else:print("non prime")