import numpy as np

#___element wise math___
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

add = arr1 + arr2
print(add)

minus = arr1 - arr2
print(minus)


multi = arr1*arr2
print(multi)

#dot product

dot = np.dot(arr1,arr2)
print(dot)

#matrix divition
trans2 = np.transpose(arr2)
div = np.dot(arr1,trans2)
print(div)

#___statical___
print(arr1.sum())
print(arr2.mean())
print(arr2.max())
