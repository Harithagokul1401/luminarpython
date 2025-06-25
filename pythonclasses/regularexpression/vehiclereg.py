#KL08BN4970   
from re import *
rule='[K][L]\d{2}[A-Z]{2}\d{4}'
regno=input("enter ypou registration number:")
matcher=fullmatch(rule,regno)
if(matcher != None):
    print("valid")
else:
    print("invalid")