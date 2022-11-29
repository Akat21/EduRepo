import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, ClassifierMixin
import collections

class NBC(BaseEstimator, ClassifierMixin):
    def __init__(self):
        pass

    def fit(self, X, y):
        '''First element = type, Second element = occurances, Third elemnt = probability'''
        P_Y = self.Single_Prob(y)
        P_X_Y = self.Condi_Prob(X, P_Y)
        # cnt = 0
        # for el in range(len(P_Y)):
        #     P_X = self.Multi_Prob(X, cnt, P_Y[el][1])
        #     P_X_Y_temp = []
        #     for col in range(len(P_X)):
        #         prob = []
        #         for i in range(len(P_X[col])):
        #             prob.append([P_X[col][i][0], (P_X[col][i][1] * P_Y[el][2])/P_Y[el][2]])
        #         P_X_Y_temp.append(prob)
        #     P_X_Y.extend(P_X_Y_temp)
        #     cnt += P_Y[el][1]
        return P_Y, P_X_Y

    def predict(self, P_Y, P_X_Y):
        pass
    
    def Single_Prob(self, y):
        P_cnt = collections.Counter(y)
        x = list(dict(P_cnt).keys())
        P = []
        for el in x:
            P.append([int(el), dict(P_cnt)[el], dict(P_cnt)[el]/sum(P_cnt.values())])
        return P

    def Condi_Prob(self, X, y):
        '''Returns probability (first dimension is first column etc)'''
        P_final = []
        el = self.Single_Prob(X[:,0])
        #TODO for every column
        for y_el_num in range(len(y)):
            P = []
            for X_el_num in range(len(el)):
                P.append([y[y_el_num][0], el[X_el_num][0], (y[y_el_num][2] * el[X_el_num][2])/y[y_el_num][2]]) #1 el - y(wartość 1 - 3), 2 el - X(wartość 1 - 3 po dyskretyzacji), 3 - prawdopodobienstwo warunkowe
            P_final.append(P)
        return P_final