import numpy as np

arr = np.array(([1, 2, 3], [4, 5, 6]))
#Reshape into custom shape
print(arr.reshape([2, 3]))

#Reshape into one dimension
flat = arr.flatten()
rav = arr.ravel()
#Both Flatten and Ravel has the same functionality
#The only difference between them is that the ravel creates a new copy of the original matrix
#While the flatten doesn't create a new copy

print(flat)
print(rav)
flat[3] = 9
print(flat)
print(arr) #Original array will not change
rav[3] = 9
print(rav)
print(arr) #Original array will change