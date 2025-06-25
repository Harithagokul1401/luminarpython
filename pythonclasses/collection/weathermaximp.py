f=open("C:\\Users\\haritha\\Desktop\\New folder\\collection\\weather.txt","r")
d={}
for k in f:
    dist,temp=k.rstrip("\n").split(",")
    # h=k.rstrip("\n").split(",")  #if a multiple coloumn data is given then use # method..assign to variavble what is needed
    #dist =h[0]
    #temp=h[1]
    # print(dist)
    # print(temp)
    if(dist not in d):
        d[dist]=temp
    else:
        old=d[dist]  #keeping the old temp in old  as district key has valu eof previouxone
        if temp>old:
            d[dist]= temp # replacing min temp of district to higher one
    

print(d)