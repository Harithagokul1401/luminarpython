#used for visuvalisation,
import matplotlib.pyplot as plt
hr=[2,4,6,8,10]
math_mrk=[23,45,67,22,45]
# to create a sccater graph 
# plt.scatter(hr,mrk)
# plt.xlabel("hour spend")
# plt.ylabel("mark scored")
# plt.title("student analysis")
# to add another line in graph
sci_mrk=[34,6,24,75,34]
plt.scatter(hr,math_mrk,label="maths")  # to label we use legend and add label to both lines
plt.scatter(hr,sci_mrk,label="science")
plt.legend()
plt.xlabel("hour spend")
plt.ylabel("mark scored")
plt.title("student analysis")
plt.show()

# to study more use matplotlib site
