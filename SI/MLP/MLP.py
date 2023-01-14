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
        X = np.column_stack((X.index, np.array(X)))
        self.w_h = np.array(len(X[0]) * [np.zeros(len(X[0]) + 1)])
        self.w_o = np.array((len(X[0]) + 1) * [np.zeros(classes)])
        self.b_h = np.array(np.ones(len(X[0]) + 1))
        self.b_o = np.array(np.ones(classes))
        out_h = self._sigmoid(np.dot(X, self.w_h) + self.b_h)
        out_o = self._sigmoid(np.dot(out_h, self.w_o) + self.b_o)
        return out_h, out_o

    def _compute_cost(self, y , out):
        final_res = np.array([0, 0, 0]).astype(float)
        for el_idx in range(len(y)):
            res = np.array(y[el_idx][1] * np.log(out[el_idx]) + (np.array([1,1,1]) - y[el_idx][1]) * np.log(np.array([1,1,1]) - out[el_idx]))
            final_res += res
        return -final_res

    def fit(self, X_train, y_train):
        X_train = np.column_stack((X_train.index, np.array(X_train)))
        w_h = np.array(len(X_train[0]) * [np.zeros(len(X_train[0]) + 1)])
        w_o = np.array((len(X_train[0]) + 1) * [np.zeros(len(y_train[0][1]))])
        b_h = np.zeros(len(X_train[0] + 1))
        b_o = np.zeros(len(y_train[0][1]))