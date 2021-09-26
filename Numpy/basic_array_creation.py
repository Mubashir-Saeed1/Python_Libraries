import numpy as np

lis = [1, 2, 3, 4, 5, 6, 7, 8]
arr = np.array(lis)
print(arr)
print(np.ndim(arr))

zero = np.zeros((2,5)) #Create array of zeros
print(zero)
twos = np.ones((2, 2)) * 2 #Create array of ones multiplied by 2
print(twos)

#Creating an array with arbitrary values
arb = np.empty((2, 3, 4))
print(arb)