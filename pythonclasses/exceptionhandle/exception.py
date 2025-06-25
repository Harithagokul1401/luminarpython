num1=int(input("enter the value of num1:"))
num2=int(input("enter the value of num2:"))
lst=[1,2,3,4,5,6]
try:
    res= num1/num2
    print("result:",res)
    pos = int(input("enter the index position :"))
    print(lst[pos])
    print("we have database transation" )
    print("file operation")
    print("process complete successfullt")
except Exception as e :
    #print("exception occured")
    print(e.args)
    # u can also write exception code  or any other code 
    # that have to run ibn caseof xceptionhere 
#agardiv by 0hai tuh it get out and wont implement baki code
# so to avoid the exception
# to avoid this we use try and except meethod
# try:
#   doubtful code
# except:
#   handling code  


# to find the position if 
# user netrerd a abnormal value then except case occur 
# to show the error like diviion and out of index then we use line as
# except exception as e: print(e.args)
# it will show appropriate msg of erroe