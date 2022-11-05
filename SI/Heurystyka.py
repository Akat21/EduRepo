import numpy as np
import matplotlib.pyplot as plt
import time

n = 4
board = [str(i) for i in range(n)]

def Best_First_Search(n, board):
    close = []
    w_row = np.array([n - (int(board[idx]) + 1) + 1 if idx < n/2 else int(board[idx]) + 1 for idx in range(len(board))])
    h1 = ((n - 1) * w_row)
    open = [el for el in board]

    while len(open) > 0:
        min_idx = np.array(np.where(h1 == min(h1))).flatten() 
        pos = open[min_idx[0]]
        del open[min_idx[0]]


        if len(pos) == n: ######WARUNEK BEZ BICIA 
            return pos
            #TODO

        else:
            t = []
            for i in range(n):
                t.append([''.join(pos) + str(i)])

        for el in t: 
            if t in close:
                continue
            else:
                sum = 0
                for e in el[0]:
                    sum += w_row[int(e)]
                h = (n - len(el[0])) * sum

            if el[0] not in open:
                open.append(el[0])
            else:
                if h < min(h1):
                    open[open.index(el[0])] = el[0]
        
        close.append(pos)
    print(close)
    print(open)
    print(pos)
    print(t)
    return null

print(Best_First_Search(n, board))