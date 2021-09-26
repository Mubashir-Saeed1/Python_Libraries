import numpy as np

arr1 = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
arr2 = np.array(([10, 11, 12], [13, 14, 15], [16, 17, 18]))

#Concatenating rows
con = np.concatenate((arr1, arr2), axis = 0)
print(con)

#Concatenating rows
print(np.vstack((arr1, arr2)))
print(np.r_[arr1, arr2])

#Concatenating Columns
print(np.hstack((arr1, arr2)))
print(np.c_[arr1, arr2])