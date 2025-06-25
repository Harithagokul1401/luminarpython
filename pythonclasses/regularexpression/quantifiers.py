import re
count =0
matcher='a+'# count for single a and group of a(a,aa,aaa,aaaa etc)
matcher="a*"# count for zero a ,single a and group of a
matcher='a?'# count for single a
matcher='a{2}'  # count for 2 a
matcher='a{2,3}' # count for 2-3 a
pattern= re.finditer(matcher,"abdbabababadsef") # to find no.of ab in that word
print(pattern)  # output of line 5 is a object
for pat in pattern:
    count+=1
    print(pat.start())  # to find the position of ab in string
    print(pat.group()) # to find which word  is matched with 
print(count)
