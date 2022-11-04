import numpy as np
import matplotlib.pyplot as plt
import time

n = 4
board = [str(i) for i in range(n)]

def Best_First_Search(n, board):
    close = []
    w_row = np.array([n - (int(board[idx]) + 1) + 1 if idx < n/2 else int(board[idx]) + 1 for idx in range(len(board))])
    h1 = (n - 1) * w_row 
    open = [board]

Best_First_Search(n, board)