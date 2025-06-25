lst=[11,2,3,4,5,6,7]
lst.sort()  #it will sort first
low=0
upp=len(lst)-1
element = int(input("entertheelement: "))
flg=0
while(low<=upp):
    mid=(upp+low)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flg=1
        break
if(flg==0):
    print("not found")
else:
    print("found")