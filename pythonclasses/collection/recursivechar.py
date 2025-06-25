pattern="ACBCBABACBCDC"
dict={}
# first recursive character
for char in pattern:
   # print(char)
    if char not in dict:
        dict[char]=1
    else:
        print("got the letter..: ",char)
        break
