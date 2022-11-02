import numpy as np
import matplotlib.pyplot as plt
import time

###inteligentne - sprawdzanie bic zawsze

def BFS(n, board, result):
    '''Possible boards using BFS'''
    counter = 0 
    counter2 = 0
    if len(board) == 0:
        for i in range(n):
            board.append([str(i)])
            counter += 1
    while len(board[0][0]) < n:
        for i in range(n):
            counter += 1
            board.append([''.join(board[0]) + str(i)])
            if len(board[-1][0]) == n:
                counter2 += 1
                board, pos = BFS_captures(board)
                if len(pos[0]) == n:
                    result.append(pos[0])
        del board[0]
        if len(board) == 0:
            break
    return result, counter, counter2

def Intel_BFS(n, board, result):
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
            board, pos = BFS_captures(board)
            if len(pos[0]) == n:
                result.append(pos)
        del board[0]
        if len(board) == 0:
            break
    return result, counter

def BFS_captures(board):
    '''Check if position is valid then delete the wrong one'''
    result = []
    for idx, el in enumerate(board[-1][0]):
        if len(board) == 0:
            break
        for idx1, el1 in enumerate(board[-1][0]):
            if idx1 > idx:
                if attack(el, idx, el1, idx1) == True:
                    del board[-1]
                    return board, "0"
                else:
                    continue
            else:
                continue
    result.append(board[-1][0])
    return board, result

def DFS(n, board, result, counter = 0, counter2 = 0):
    '''Possible boards using DFS'''
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
                counter2 += 1
                board = DFS_captures(board)
        if len(board) == 0:
                    break
    if len(board) != 0:
        result.append(board[-1][0])
        del board[-1]
        if len(board) != 0:
            return DFS(n, board, result, counter, counter2)
        else:
            return result, counter, counter2
    else:
        return result, counter, counter2


def Intel_DFS(n, board, result, counter = 0):
    '''Possible boards using DFS'''
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
            board = DFS_captures(board)
        if len(board) == 0:
            break
    if len(board) != 0:
        result.append(board[-1][0])
        del board[-1]
        if len(board) != 0:
            return Intel_DFS(n, board, result, counter)
        else:
            return result, counter
    else:
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
    data = []
    for n in range(x,y):
        board = []
        result = []

        start1 = time.time()
        board_1, counter, counter2 = DFS(n,board,result)
        print("\nDFS n:",n,"\nWynik:", board_1, "\nLiczba stanów wygenerowanych:", counter)
        end1 = time.time()
        print("Czas wykonania:", end1 - start1)
        data.append([counter, counter2, end1-start1])

    data = np.array(data)
    fig, ax = plt.subplots()
    range1 = np.arange(len(data))
    ax.bar(x = range1, height = data[:,0],width = 0.12,label = "Stany wygenerowane")
    ax.bar(x = range1+0.12, height = data[:,1],width = 0.12,label = 'Stany sprawdzone')
    ax.bar(x = range1+0.12*2, height = data[:,2]*10000,width = 0.12,label = 'Czas x10000')
    ax.set_xticks(np.arange(len(data)))
    ax.set_xticklabels(["n = " + str(i) for i in range(x,y)])
    ax.legend()
    plt.savefig("Plot.png", format = "png")
    plt.show()

def BFS_DFS_Comparision(x, y):
    data_BFS = []
    data_DFS = []
    for n in range(x,y):

        board = []
        result = []

        start1 = time.time()
        board_1, counter, counter2 = BFS(n,board,result)
        print("\nBFS n:",n,"\nWynik:", board_1, "\nLiczba stanów wygenerowanych:", counter)
        end1 = time.time()
        print("Czas wykonania:", end1 - start1)
        data_BFS.append([counter, counter2, end1-start1])

        board = []
        result = []

        start1 = time.time()
        board_1, counter, counter2 = DFS(n,board,result)
        print("\nDFS n:",n,"\nWynik:", board_1, "\nLiczba stanów wygenerowanych:", counter)
        end1 = time.time()
        print("Czas wykonania:", end1 - start1)
        data_DFS.append([counter, counter2, end1-start1])
    
    data_BFS = np.array(data_BFS)
    fig, ax = plt.subplots(2)
    range1 = np.arange(len(data_BFS))
    ax[0].bar(x = range1, height = data_BFS[:,0],width = 0.12,label = "Stany wygenerowane")
    ax[0].bar(x = range1+0.12, height = data_BFS[:,1],width = 0.12,label = 'Stany sprawdzone')
    ax[0].bar(x = range1+0.12*2, height = data_BFS[:,2]*10000,width = 0.12,label = 'Czas x10000')
    ax[0].set_xticks(np.arange(len(data_BFS)))
    ax[0].set_xticklabels(["n = " + str(i) for i in range(x,y)])
    ax[0].legend()
    ax[0].set_title("BFS")

    data_DFS = np.array(data_DFS)
    range1 = np.arange(len(data_DFS))
    ax[1].bar(x = range1, height = data_DFS[:,0],width = 0.12,label = "Stany wygenerowane")
    ax[1].bar(x = range1+0.12, height = data_DFS[:,1],width = 0.12,label = 'Stany sprawdzone')
    ax[1].bar(x = range1+0.12*2, height = data_DFS[:,2]*10000,width = 0.12,label = 'Czas x10000')
    ax[1].set_xticks(np.arange(len(data_DFS)))
    ax[1].set_xticklabels(["n = " + str(i) for i in range(x,y)])
    ax[1].legend()
    ax[1].set_title("DFS")
    plt.savefig("Plot.png", format = "png")
    plt.show()



def BFS_DFS_Intelligent_Comparision(x, y):
    data_BFS = []
    data_DFS = []
    for n in range(x,y):

        board = []
        result = []

        start1 = time.time()
        board_1, counter = Intel_BFS(n,board,result)
        print("\nBFS n:",n,"\nWynik:", board_1, "\nLiczba stanów wygenerowanych:", counter)
        end1 = time.time()
        print("Czas wykonania:", end1 - start1)
        data_BFS.append([counter, end1-start1])

        board = []
        result = []

        start1 = time.time()
        board_1, counter = Intel_DFS(n,board,result)
        print("\nDFS n:",n,"\nWynik:", board_1, "\nLiczba stanów wygenerowanych:", counter)
        end1 = time.time()
        print("Czas wykonania:", end1 - start1)
        data_DFS.append([counter, end1-start1])

    data_BFS = np.array(data_BFS)
    fig, ax = plt.subplots(2)
    range1 = np.arange(len(data_BFS))
    ax[0].bar(x = range1, height = data_BFS[:,0],width = 0.12,label = "Stany wygenerowane")
    ax[0].bar(x = range1+0.12, height = data_BFS[:,1]*10000,width = 0.12,label = 'Czas x10000')
    ax[0].set_xticks(np.arange(len(data_BFS)))
    ax[0].set_xticklabels(["n = " + str(i) for i in range(x,y)])
    ax[0].legend()
    ax[0].set_title("BFS")

    data_DFS = np.array(data_DFS)
    range1 = np.arange(len(data_DFS))
    ax[1].bar(x = range1, height = data_DFS[:,0],width = 0.12,label = "Stany wygenerowane")
    ax[1].bar(x = range1+0.12, height = data_DFS[:,1]*10000,width = 0.12,label = 'Czas x10000')
    ax[1].set_xticks(np.arange(len(data_DFS)))
    ax[1].set_xticklabels(["n = " + str(i) for i in range(x,y)])
    ax[1].legend()
    ax[1].set_title("DFS")
    plt.savefig("Plot.png", format = "png")
    plt.show()


board = []
result = []

print(BFS_DFS_Intelligent_Comparision(4, 10))