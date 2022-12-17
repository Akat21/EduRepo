from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import random
from Perceptron import Perceptron
from sklearn.model_selection import train_test_split

m = 20

X, y = datasets.make_blobs(n_samples=m, centers=2, n_features=2, center_box=(80,100))

X = np.column_stack((np.ones(len(X)), X))

plt.plot(X[:, 1][y==0], X[:,2][y==0], 'g^')
plt.plot(X[:,1][y==1], X[:,2][y==1], 'bs')
# plt.show()

X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.33)

p1 = Perceptron(0.1)
p1.fit(X_train, y_train)

predicted = np.array(p1.predict(X_test))

predicted[predicted == -1] = 0
print(predicted == y_test)
