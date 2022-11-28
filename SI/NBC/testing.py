import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, ClassifierMixin
from NBC import NBC 

X = np.genfromtxt(fname = 'NBC/wine.data', delimiter = ',', )
y = X[:,0]
X = X[:,1:]

est = KBinsDiscretizer(n_bins = 3)

X_train, X_test = train_test_split(X)

nbc = NBC()
P_X, P_X_Y = nbc.fit(X,y)
print(P_X, P_X_Y)