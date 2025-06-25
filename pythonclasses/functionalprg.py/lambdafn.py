# functional prg : to reduce lenght of the code
# 1.lambda  is anonymous(unnamed) function
# 2.map
# 3.filter
# 4.list comprehension
# 5. reduce

#1. lambda : like for the addition we use function andthen we have to call here in a single line operation is donr
f=lambda n1,n2: n1+n2  # no brackets
print(f(10,20))
f=lambda n1,n2:n1-n2
print(f(10,20))


# 2 map function : map(function,iterables) 
# if A OPERATION has to be done in entire values at a time then this isused
# no of input = no.of  output
# ex:
# 1.for somevalues we need to find the square of each number ad for normally we use for Loop
# [10,20,30,40]=[100,400,900,1600]
# 2. for converting lower case to upper case 
# [ab,cd,ef,gh]=[AB,CD,EF,GH]

lst=[1,2,3,4] # to find square of each number
def square(num):
    return num*num
sq=(map(square,lst)) # converted to list varna it is map type o/p =<map object at 0x0000023E700AB4C0> it shows address of object

print(sq)


# 3.filter = filter(function,iterables)
# ex
# no of input is not equal to no. of output
# [1,2,3,5,6,7,8]=[2,4,6,8] 
# [ab,ad,fv,gh]=[ab,ad] => outout sirf a se start hone valachahiye
def evens(num):
    return num%2==0
eves=list(filter(evens,lst))
print(eves)
# usinf lambda
eve=list(filter(lambda num:num%2==0,lst))
print(eve)