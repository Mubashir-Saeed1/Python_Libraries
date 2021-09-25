import numpy as np

#Creating array
mat = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))

#Finding Diagonal Elements
dgnl = np.diag(mat)
print(dgnl)

#Finding Eigen values
eig = np.linalg.eig(mat)
print(eig)

#Finding inverse of the matrix
inve = np.linalg.inv(mat)
print(inve)

#Finding the sum of diagonal elements of a matrix
print("Trace: ", mat.trace())

#Finding decomposition of a Matrix
dec = np.linalg.svd(mat)
print(dec)

#Calculating dot product of two matrices
print(np.dot(np.array([4, 5, 6]), np.array([6, 3, 9])))

#Finding the determinant of the matrix
deter = np.linalg.det(mat)
print(deter)