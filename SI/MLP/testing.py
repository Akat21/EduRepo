import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from MLP import MLP

y_iris_coded = []
X_iris, y_iris = fetch_openml(name = 'iris', version = 1, return_X_y = True)

for idx, el in enumerate(y_iris):
    if el == 'Iris-setosa':
        y_iris_coded.append([idx + 1, [1,0,0]])
    elif el == 'Iris-versicolor':
        y_iris_coded.append([idx + 1, [0,1,0]])
    elif el == 'Iris-virginica':
        y_iris_coded.append([idx + 1, [0,0,1]])

X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris_coded, random_state = 13)

mlp = MLP()
res = mlp.fit(X_train, y_train)
# print(J)
