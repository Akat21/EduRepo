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
        self.P_Y = self.Single_Prob(y)
        self.P_X_Y = self.Condi_Prob(X, y)
        return self.P_Y, self.P_X_Y

    def predict(self, P_X):
        print(P_X)
        res = []
        cnt = 0
        for el in P_X:
            P = []
            for classi_num in range(1,len(self.P_Y)+1):
                prob = 1
                for col in self.P_X_Y:
                    for classi in col:
                        if classi[0][0] == classi_num:
                            for est in classi:
                                if est[1] == el[cnt]:
                                    prob *= est[2]
                                    cnt += 1 
                                    break
                            break
                cnt = 0       
                prob *= self.P_Y[classi_num - 1][2]
                P.append(prob)
            res.append(P.index(max(P)) + 1)
        return res
    
    def Single_Prob(self, y):
        P_cnt = collections.Counter(y)
        x = list(dict(P_cnt).keys())
        P = []
        for el in x:
            P.append([int(el), dict(P_cnt)[el], dict(P_cnt)[el]/sum(P_cnt.values())])
        return P

    def Condi_Prob(self, X, y):
        '''Returns probability (first dimension is first column etc)'''
        P_semifinal = []
        P_final = []
        P_Y = self.Single_Prob(y)

        for col_num in range(len(X[0])):
            P_semifinal = []
            for y_el_num in range(len(P_Y)):
                P = []
                P_X = []

                ##Liczymy prawdopodobienstwo wystąpienia estymowanej wartosci X dla kolumny w kazdym estymatorze y(są 3 - 1,2,3)
                for idx, est in enumerate(y):
                    if est == P_Y[y_el_num][0]:
                        P_X.append(X[idx, col_num])
                P_X = self.Single_Prob(P_X)
                print(P_X)
                
                ##Jeżeli nie ma wszystkich wartości w kolumnie dodajemy kolumne o prawdopodobienstwie 0.0 dla brakujacego elementu
                ##nwm czy potrzebne

                est_num = set(X[:,0])
                for el in P_X:
                    if el[0] in est_num:
                        est_num.remove(el[0])
                if len(list(est_num)) > 0:
                    for el in list(est_num):
                        P_X.append([int(el), 0, 0.0])

                ##Liczymy prawdopodobieństwo warunkowe dla każdego elementu i dodajemy do listy P
                ## Dzielenie przez P_Y to liczba występowania y czy jego prawdopodobienstwo??? ( jako liczba wystepowania nie dziala)
                for X_el_num in range(len(P_X)):
                    P.append([P_Y[y_el_num][0], P_X[X_el_num][0], (P_Y[y_el_num][2] * P_X[X_el_num][2])/P_Y[y_el_num][1]]) #1 el - y(wartość 1 - 3), 2 el - X(wartość 1 - 3 po dyskretyzacji), 3 - prawdopodobienstwo warunkowe
                
                P_semifinal.append(P)
            P_final.append(P_semifinal)
        return np.array(P_final)