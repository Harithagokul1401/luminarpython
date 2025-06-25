from re import *
rule='[K][L]0-9{2}A-Z{2}0-9{4}'
f=open("regularexpression/vehregno.txt","r")
for items in f:
    item=items.strip("\n") 
    print(item)
    match=fullmatch(rule,items)
    if(match !=None):
       print("valid")
    else:
       print("invalid ")
       










        