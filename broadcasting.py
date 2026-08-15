import numpy as np

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

# scalar+array
add1 = arr1 + 10
print(add1)

#line addiction
add2 = arr1 + np.array([10,11])
print(add2)

#column addiction

add3 = arr1 + np.array([[10],[11]])

#1D + 2D

a = np.array([1,2,3])
n = np.array([[4,5,6],[7,8,9],[10,11,12]])
add3 = a+n
print(a+n)