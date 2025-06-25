bdate =  int(input("birth date : "))
bmonth = int(input(" birth month : "))
byear = int(input(" birth year : "))
cdate = int(input(" current date : "))
cmonth = int(input(" current month : "))
cyear = int(input(" current year : "))
yr = cyear - byear
mon = cmonth - bmonth 
dat = cdate - bdate
print(dat)
if(dat>0):
    date = 31 - dat
else:
    date= 31 + dat
if (date<=31):
    month = mon-1
else:
    month = mon
print(" your current age is :", yr,"year",month,"month",date,"days old" )
