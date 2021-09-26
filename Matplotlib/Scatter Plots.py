import matplotlib.pyplot as plt
import pandas
from sklearn.datasets import load_iris

iris = load_iris()
print(iris)
features = iris.data.T
print("Feature 3: ", features[3])
plt.scatter(features[0], features[1],alpha=0.2, s=100*features[3], c=iris.target, cmap='plasma')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()