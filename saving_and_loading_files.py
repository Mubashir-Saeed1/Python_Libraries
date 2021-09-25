import numpy as np

name = np.array(['Mubashir', 'Hassan', 'Jamshid', 'Qaisar', 'Zeeshan'])
regNo = np.array([1630, 1669, 1654, 1627, 4477])

#Sorting the Array
sorte = np.sort(regNo)
print(sorte)

#Saving a Single array
np.save('names', name)
np.save('Numbers', regNo)

#Loading Files
names = np.load('names.npy')
print(names)
numbers = np.load('Numbers.npy')
print(numbers)

#Saving & multiple arrays in single file
np.savez('inf', name = name, no = regNo)

file = np.load('inf.npz')
print("Names: ", file['name'])
print("Registration Numbers: ", file['no'])
