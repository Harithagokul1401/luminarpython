from re import *
rule='[6-9]\d{9}'  # check for []use it toseperate 
phno=input("enter the phonenumber: ")
matcher=fullmatch(rule,phno)
if(matcher != None):
    print("valid number")
else:
    print("invalid number")