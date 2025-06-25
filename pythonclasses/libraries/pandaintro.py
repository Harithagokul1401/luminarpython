 
import pandas as pd # type: ignore
# data  frame is important part in form of table 
# data  frame for 3 person with their age

# people:p1,p2,p3
#age: 20,30,50
# write it as a dictionary people as key  and its value as a list
d={'people':['p1','p2','p3'],'age':[20,30,50]}
df=pd.DataFrame(d)
#print(df)
#u can create dataframe from excel sheet
print(pd.read_excel("libraries/exam.xlsx"))
# to read from csv file then 
#pd.read_csv("folder path")

#tget details of student of with above particular mrk
# df[df["score"]>=300]]
# and in thatto u want particular colounm only then 
#df[df[score>300]["people"]] syntax
#df[df[condition][colm][colm2]...]
