import numpy as np

class MLP(object):
    def __init__(self, hidden = 5, epochs = 100, eta = 0.1, shuffle = True):
        self.hidden = hidden
        self.epochs = epochs
        self.eta = eta
        self.shuffle = shuffle

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def _forward(self, X):
        classes = 3
        self.w_h = np.array(len(X) * [np.zeros(self.hidden) + 0.01])
        self.w_o = np.array(self.hidden * [np.zeros(classes) + 0.01])
        self.b_h = np.array(np.ones(self.hidden))
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
        X_train = np.array(X_train)
        y_train = np.column_stack(((np.array(y_train)[:,0] - 1), np.array(y_train)[:,1]))
        w_h = np.random.randn(len(X_train[0]), self.hidden)
        w_o = np.random.randn(self.hidden, len(y_train[0][1]))
        b_h = np.zeros(self.hidden)
        b_o = np.zeros(len(y_train[0][1]))

        #SHUFFLE 
        if self.shuffle == True:
            idxs = np.arange(X_train.shape[0])
            np.random.shuffle(idxs)
            X_train = X_train[idxs]
            y_train = y_train[idxs]
        
        ran_idx = np.random.randint(len(X_train), size = len(X_train))
        for idx in ran_idx:
            a_h, a_o = self._forward(X_train[idx])
            f_o = (a_o * (1 - a_o))
            delta_o = (a_o - y_train[idx,1]) * f_o
            f_h = (a_h * (1 - a_h))
            delta_h = np.dot(delta_o, np.transpose(w_o)) * f_h
            _X_train = np.insert(X_train[idx], 0, 1)
            grad_w_h = np.dot(np.transpose(_X_train), delta_h)
            grad_b_h = delta_h
            grad_w_o = np.dot(np.transpose(a_h), delta_o)
            print(grad_w_o)
            break
            ##GRADINET TODO