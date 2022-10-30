import numpy as np
import matplotlib.pyplot as plt
import time

###inteligentne - sprawdzanie bic zawsze

def DFS(n, board, result):
    '''Possible boards using DFS'''
    counter = 0
    if len(board) == 0:
        for i in range(n):
            board.append([str(i)])
            counter += 1
    while len(board[-1][0]) < n:
        last_el = board[-1] 
        del board[-1]
        for i in range(n):
            counter += 1
            board.append([''.join(last_el) + str(i)])
            if (len(board[-1][0]) == n):
                board = DFS_captures(board)
        if len(board) == 0:
                    break
    if len(board) != 0:
        result.append(board[-1][0])
        del board[-1]
        return DFS(n, board, result)
    else:
        return result, counter

def BFS(n, board, result):
    '''Possible boards using BFS'''
    counter = 0 #TODO
    if len(board) == 0:
        for i in range(n):
            board.append([str(i)])
            counter += 1
    while len(board[0][0]) < n:
        for i in range(n):
            counter += 1
            board.append([''.join(board[0]) + str(i)])
        del board[0]
        if len(board[0][0]) == n:
            board, result = BFS_captures(board)
    return result, counter

def DFS_captures(board):
    '''Check if position is valid then delete the wrong one'''
    for idx, el in enumerate(board[-1][0]):
        if len(board) == 0:
            break
        for idx1, el1 in enumerate(board[-1][0]):
            if idx1 > idx:
                if attack(el, idx, el1, idx1) == True:
                    del board[-1]
                    break
                else:
                    continue
            else:
                continue
    return board

def BFS_captures(board):
    '''Check if position is valid'''
    result = []
    is_captured = False
    for pos in board:
        for idx, el in enumerate(pos[0]):
            for idx1, el1 in enumerate(pos[0]):
                if idx1 > idx:
                    if attack(el, idx, el1, idx1) == True:
                        is_captured = True
                        break
                    else:
                        is_captured = False
            if is_captured == True:
                break
        if is_captured == False:
            result.append(pos[0])
    return board, result

def attack(qrow, qcolumn, orow, ocolumn):
    '''Check if there is possible capture'''
    if int(qrow) == int(orow):
        return True
    elif int(qcolumn) == int(ocolumn):
        return True
    elif abs(int(qrow) - int(orow)) == abs(int(qcolumn) - int(ocolumn)):
        return True
    else:
        return False

def DFS_Stats(x,y):
    for n in range(x,y):
        board = []
        result = []

        start1 = time.time()
        board_1, counter = DFS(n,board,result)
        print("\nDFS n:",n,"\nWynik:", board_1, "\nLiczba stanów wygenerowanych:", counter)
        end1 = time.time()
        print("Czas wykonania:", end1 - start1)

def BFS_DFS_Comparision(x, y):
    for n in range(x,y):

        board = []
        result = []

        start1 = time.time()
        board_1, counter = BFS(n,board,result)
        print("\nBFS n:",n,"\nWynik:", board_1, "\nLiczba stanów wygenerowanych:", counter)
        end1 = time.time()
        print("Czas wykonania:", end1 - start1)

        board = []
        result = []

        start1 = time.time()
        board_1, counter = DFS(n,board,result)
        print("\nDFS n:",n,"\nWynik:", board_1, "\nLiczba stanów wygenerowanych:", counter)
        end1 = time.time()
        print("Czas wykonania:", end1 - start1)

DFS_Stats(4,11)
#BFS_DFS_Comparision(4,8)