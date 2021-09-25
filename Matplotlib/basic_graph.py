import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1, 2, 3, 4, 5, 6]
y = [2.61, 3.13, 2.63, 2.77, 3.09, 3.36]

plt.title("Basic Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(
    x,
    y,
    label="2x",
    color="red",
    linewidth=3,
    marker=".",
    linestyle="--",
    markersize=20,
    markeredgecolor="blue",
)
plt.xticks([1, 2, 3, 4, 5, 6])
plt.yticks([2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4])
plt.legend()
plt.show()


j = np.arange(1, 5, 1)
k = np.arange(1, 9, 2)

t = np.arange(1, 10, 0.1)
r = np.arange(1, 91, 1)

plt.title("Basic Graph 2")
plt.xlabel("J")
plt.ylabel("K")
plt.plot(j, k, "r.--", markersize=20, label="2x")
plt.plot(t, r)
plt.legend()
plt.show()