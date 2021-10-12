from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = load_iris()
x = iris.data
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names

# print("Data: ", x)
# print("Target: ", y)

# print("Feature Names: ", feature_names)
# print("Target Names", target_names)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=1)

classifier_knn = KNeighborsClassifier(n_neighbors = 3)
classifier_knn.fit(x_train, y_train)

y_predict = classifier_knn.predict(x_test)
print("Accuracy: ", metrics.accuracy_score(y_test, y_predict))

