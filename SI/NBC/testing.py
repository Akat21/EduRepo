import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, ClassifierMixin
from NBC import NBC 

X = np.genfromtxt(fname = 'wine.data', delimiter = ',', )
y = X[:,0]
X = X[:,1:]

est = KBinsDiscretizer(n_bins = 3, encode='ordinal', strategy='uniform').fit(X)
X = est.transform(X)

X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.33, random_state=42)

nbc = NBC()
P_Y, P_X_Y = nbc.fit(X_train,y_train)
print(P_X_Y)