# lst=[10,20,31,40,50,607,70,80,9063,100]
# for i in lst:
#     if (i%2 ==0):
#         print(i)

lst=[]
od=[]
eve=[]
for i in range(1,101):
    if(i%2==0):
        eve.append(i)  # append() not append[]
    else:
        od.append(i)


print(" even : ",eve)
print(" odd : ", od)