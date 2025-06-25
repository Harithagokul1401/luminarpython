employee={"id":101,
          "name":"hari",
          "desig":"developer",
          "sal":30000}

print(employee["name"])
employee["company"]="luminar"           #add  company
print(employee)
employee["sal"] +=5000                      #update salary
print(employee)
for key in employee:
    print(key," : ",employee[key])