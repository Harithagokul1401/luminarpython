f=open("fileoperation/numbers.txt","r")
lst=[]
eve=[]
od=[]
for lines in f:
    #line=int(lines)
    lst.append(int(lines.rstrip("\n")))
print(lst)
for num in lst:
    if(num%2==0):
        eve.append(num)
    else:
        od.append(num)
print("even number :",eve)
print("odd number :",od) 