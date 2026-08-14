#array creation in numpy

import numpy as np

# array making from list
arr=np.array([1,2,3,4])
print(arr)
print(type(arr))

zeros=np.zeros((3,3))
print(zeros)
print(type(zeros))

ones=np.ones((3,3))
print(ones)
print(type(ones))

range=np.arange(0,30,6)
print(range)
print(type(range))

linespace=np.linspace(5,50,20)
print(linespace)
print(type(linespace))

