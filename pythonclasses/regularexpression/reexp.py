# for pattern matching => regular expression
# step 1 : we have to import remodule
import re
count =0
pattern= re.finditer("ab","abdbabababadsef") # to find no.of ab in that word
print(pattern)  # output of line 5 is a object
for pat in pattern:
    count+=1
    print(pat.start())  # to find the position of ab in string
    print(pat.group()) # to find which word  is matched with 
print(count)
