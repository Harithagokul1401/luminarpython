# lst = [1,2,3,4,12,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99,100]
# n = int(input("enter your number :"))
# flag =0
# for i in lst:
#     if (i==n):
#         print("hurray !!!!! i got it")
#         flag = 1

# if(flag == 0):
#     print("opps!! i didnt fint it")

lst=[1,2,3,4,5,6]
n = int(input("enter the number : "))
x = len(lst)
for i in range(0,x):
    for j in range(i+1,x):
        s = lst[i] +lst[j]
        if( n==s):
            print("your input is",n,"sum  of", lst[i],"+",lst[j])
    