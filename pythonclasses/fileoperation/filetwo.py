f=open("fileoperation/numbers.txt","r")
lst=[]
for num in f:
    lst.append(int(num.rstrip("\n"))) #remove \n but still its a string so its better to se line 10 --> to avoid str use int in front
      #rstip -> to remove from end (trailing char)----lstrip-> to remove front char(leading char)
    
    #lst.append(num)
#print(lst)     #101\n', '102\n', '103\n', '104\n', '105\n', '106\n', '107\n', '108\n', '109\n', '110\n', '111\n', '112\n', '113\n', '114']
# to remove \n 2 way
#1, lst.append(int(num))   --> simple direct int milega
#2  from line 4


print(lst)
print(sum(lst))