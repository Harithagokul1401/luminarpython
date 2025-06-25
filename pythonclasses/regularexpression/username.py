#a-k  first
# second no divisibleby 3 [369]
# then any 
from re import *

rule='[a-k][369][a-zA-Z0-9]*'  # no lenght so *
var=input("enter the variable name: ")
matcher=fullmatch(rule,var)
if (matcher!=None):
    print("valid")
else:
    print("not valid")