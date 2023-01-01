import numpy as np

class MLP(object):
    def __init__(self, hidden = 10, epochs = 100, eta = 0.1, shuffle = True):
        self.hidden = hidden
        self.epochs = epochs
        self.eta = eta
        self.shuffle = shuffle

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    