import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 3, 4, 5, 6, 7, 8, 9]
plt.hist(x, bins=3) #Bins is the number of divisions
plt.xticks(x)
plt.ylabel('Number of Appearances')
plt.show()

r = np.random.rand(1000)
plt.hist(r, bins= 20)
plt.xlabel('0 to 1000')
plt.ylabel('Number of Appearances')
plt.show()