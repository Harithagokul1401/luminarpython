employees=[[1001,"rahul",14000],
           [1002,"rahula",13000],
           [1003,"rahuls",16000],
           [1004,"rahuld",15000],
           [1005,"rahulk",19000]]

#for emp in employees:
#    print(emp[1])       #to only print names 
  #  print(emp)     #[1001, 'rahul', 14000]
                    # [1002, 'rahula', 13000]
                    # [1003, 'rahuls', 16000]
                    # [1004, 'rahuld', 15000]
                    # [1005, 'rahulk', 19000]

#toprint the name with salary above 15k

for emp in employees:
    if(emp[2]>=15000):
        print(emp[1])



