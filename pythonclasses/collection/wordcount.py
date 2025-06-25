line="One day a hare was showing off how fast he could run. He laughed at the turtle for being so slow After seeing the overconfidence " \
"the turtle moved him to a race The hare (rabbit) laughed at the turtle test and he accepted his demand"
words = line.split(" ")
print(words)   # word by defaulti a list
dict={}
for word in words:
    if word not in dict:
        dict[word]= 1
    else:
         dict[word] +=1

for key in dict:
    print(key," - ",dict[key])
