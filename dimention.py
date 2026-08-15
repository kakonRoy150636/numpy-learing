import numpy as np

arr=np.array([[1,2,3],[4,5,6]])

print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)

print(arr)

#reshape
reshape = arr.reshape(3,2)
print(reshape)

re = arr.reshape(2,3)
print(re)

#flatten
flat = arr.flatten()
print(flat)

#transpose
trans = arr.T
print(trans)
print(arr.size)