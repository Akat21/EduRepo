import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, ClassifierMixin
import collections

class NBC(BaseEstimator, ClassifierMixin):
    def __init__(self):
        pass

    def fit(self, X, y):
        '''First element = type, Second element = probability'''
        P_Y = self.Single_Prob(y)
        return P_Y

    def Single_Prob(self, y):
        P_cnt = collections.Counter(y)
        x = list(dict(P_cnt).keys())
        P = []
        for el in x:
            P.append([int(el),dict(P_cnt)[el]/sum(P_cnt.values())])
        return P