from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import random 

def fs(x):
    return np.where(x > 0 , 1, -1)

class Perceptron:
    def __init__(self, learning_rate):
        self.lr = learning_rate
        self.weights = None
        self.k = None

    def fit(self, X, y): #########CZASAMI NIE ZNAJDUJE WSPOLCZYNNIKA
        n_samp, n_features = X.shape
        E = np.zeros(n_samp)

        self.weights = np.zeros(n_features)
        self.k = 0

        y_fs = fs(y)

        while(True):
            E = fs(np.dot(X, self.weights))
            if len(list(set(y_fs == E))) == 1:
                if list(set(y_fs == E))[0] == True:
                    break

            r_idx = random.randint(0, len(X)-1)

            update = self.lr * (y_fs[r_idx] - E[r_idx])
            self.weights = self.weights + (update * X[r_idx])
            self.k += 1

    def predict(self, X):
        return fs(np.dot(X,self.weights))