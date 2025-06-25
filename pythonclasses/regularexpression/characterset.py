from re import *
#pattern = "[abc]" # either check for a,b,c
#pattern='[a-z]' # check for lowercase a-z character : wont match with  space ad number
#pattern='[A-Z]'
pattern='[a-zA-Z]'  # [A-z] also work
#[0-9]   for [^0-9] print except digit      for special char=[^a-zA-Z0-9]
matcher=finditer(pattern,"abc sbAbaba bcdbsba XCV#$bcaba")
for match in matcher:
    print(match.start())
    print(match.group())

# for predefine char
#pattern='\s'  check for all space
#pattern='\d'  check for digits this can be used instead fo '[0-9]'
#pattern='\D   ^[0-9]
#pattern='\w'  every characterexcept special char
#pattern='\W'   special char
