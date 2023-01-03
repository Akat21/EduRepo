import numpy as np

class MLP(object):
    def __init__(self, hidden = 10, epochs = 100, eta = 0.1, shuffle = True):
        self.hidden = hidden
        self.epochs = epochs
        self.eta = eta
        self.shuffle = shuffle

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def _forward(self, X):
        classes = 3
        self.w_h = np.array(len(X[0]) * [np.ones(len(X[0]))])
        self.w_o = np.array(len(X[0]) * [np.ones(classes)])
        self.b_h = np.array(np.ones(len(X[0])))
        self.b_o = np.array(np.ones(classes))

        out_h = self._sigmoid(np.dot(X, self.w_h) + self.b_h)
        out_o = self._sigmoid(np.dot(out_h, self.w_o) + self.b_o)
        return out_h, out_o

    