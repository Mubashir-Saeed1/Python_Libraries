import numpy as np

lis = [1, 2, 3, 4, 5, 6, 7, 8]
arr = np.array(lis)


#Where() Function of Numpy. This is same as we use in MySQL
arr = np.where(arr >= 5, 2, arr)
print(arr)

#Taking Transpose of a matrix
matr = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(matr)
print(np.transpose(matr))

#Transpose can also be taken as
print(matr.T)

#Calculating Cumsum of the matrix
cums = np.cumsum(matr)
print(cums)

#Calculating Cumproduct of the matrix
cump = np.cumprod(matr)
print(cump)

#Calculating Mean of the matrix Column wise
meanColumn = np.mean(matr, axis=1)
print(meanColumn)

#Calculating Mean of the matrix Row wise
meanRow = np.mean(matr, axis=0)
print(meanRow)

#Boolean Functions
arr = np.array(lis)
arr1 = arr>4
print(arr1)
print(arr1.any())
print(arr1.sum())
print(arr1.all())
