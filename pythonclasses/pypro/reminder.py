n1= int(input("enter the first number: "))
n2= int(input("enter the second number: "))
q=0
while(n1>=n2):
    n1=n1-n2
    q+=1
print("rem = ",n1)
print("qut= ",q)