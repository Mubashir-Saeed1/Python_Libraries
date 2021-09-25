import numpy as np

lis = [1, 2, 3, 4, 5, 6, 7, 8]
arr = np.array(lis)

#Creating an array in range from 0 to 100 with step size of 2
hun = np.arange(0, 100, 2)
twoHun = np.arange(0, 200, 4)

#Addition of two arrays
addition = hun + twoHun
print(addition)

#Subtraction of two arrays
subtraction = addition - twoHun
print(subtraction)

#Multiplication of two arrays
multiplication = subtraction * addition

#Division of two arrays
division = multiplication/subtraction

#Comparing the elements of two arrays
print(addition == subtraction)

#Multiplying each element of the array with 2
print(arr ** 2)

#Checking if elements of the array are greater than 4 or not
print(arr>4)

#Slicing in Numpy arrays is same as we do in Python lists

#Taking Square root of all the elements of the Array.
sq = np.sqrt(twoHun)
print(sq)
