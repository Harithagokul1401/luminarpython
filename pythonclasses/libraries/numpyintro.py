#  What is NumPy?
# ✅ Numerical Python
# ✅ A powerful library for numerical computing
# ✅ Provides arrays, mathematical functions, and more!

# 🔹 Why Use NumPy?
# ✅ Efficient arrays (numpy.ndarray) — faster and more memory-efficient than regular Python lists.
# ✅ Vectorized operations — no need for slow Python loops.
# ✅ Mathematical functions — like mean, std, sin, cos, etc.
# ✅ Linear algebra, random number generation, and Fourier transforms — all built-in!

# 🔹 Example:
# python
# Copy
# Edit
import numpy as np # type: ignore                                          

# What’s # type: ignore in Python?
# ✅ It’s a special comment used when working with type checkers like mypy or Pyright (or in editors like VS Code with Pylance).
# ✅ It tells the type checker to ignore errors on that specific line.




# Create an array
arr = np.array([1, 2, 3, 4])
print(arr)  # [1 2 3 4]

# Array operations
print(arr + 10)     # [11 12 13 14]
print(arr * 2)      # [2 4 6 8]

# Mathematical functions
print(np.mean(arr))  # 2.5
print(np.sqrt(arr))  # [1. 1.414 1.732 2.]

# Multidimensional arrays
matrix = np.array([[1, 2], [3, 4]])
print(matrix)
# [[1 2]
#  [3 4]]
# 🔹 Key Benefits of NumPy:
# ✅ Speed — much faster than Python lists.
# ✅ Memory-efficient — better for large datasets.
# ✅ Powerful — essential for data science, machine learning, and scientific computing.



# arr= np.array([1,2,3,4,5,6])
# arr.shape  ==> (6,)
# arr.reshape(2,3) ==> 1 2 3
#                       4 5 6  in matrix form


##numpy is used to read images a s images are nothing but rgb vakues and
#they are been measured in pixel

#numpy as broadcast(as one operation is applied to every element)
arr+1 #=> output me sab me 1 add hoga

#dot product in matrix
m1 = np.array([1,2],[3,4])
m2 = np.array([5,6],[7,8])
np.dot(m1,m2)  #==> ([19,22]
#                    [43,50])

#also mean of arrray
np.mean(arr)  # => give u mean od array
np.std(arr)   # => give u a standard diviasion
np.random.rand(2)  #=> array([give u a random decimal number b/w 0-1])
arr=[1,2,3,np.nan,5,6]  # => [1,2,3,nan,5,6]  not  a number

# how powerful is numpy

lst=list(range(10))  #=>[0,1,2,3,4,5,6,7,8,9]
sum(lst)#  take more Time
lst=np.arr[lst]
np.sum(lst) # take less time 

#always remember before using numpy covert it to numpy line 70
#then use numpy operation
  
## do study abouut difference python list and numpy