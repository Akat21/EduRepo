import time
import matplotlib.pyplot as plt
import numpy as np


def board_gen(n, board):
    '''Board Generation using BFS'''
    counter = 0
    if len(board) == 0:
        for i in range(n):
            board.append([str(i)])
            counter += 1
    while len(board[0][0]) < n:
        for i in range(n):
            counter += 1
            board.append([''.join(board[0]) + str(i)])
        del board[0]
    print("Liczba stanów wygenerowanych: ", counter)
    return board, counter
    
def capturing(board):
    '''Captures in every position'''
    cnt = 0
    result = []
    for pos in board:
        score = 0
        cnt += 1
        for idx, el in enumerate(pos[0]):
            for idx1, el1 in enumerate(pos[0]):
                if idx1 > idx:
                    if attack(el, idx, el1, idx1) == True:
                        score += 1
        result.append([score,pos])
    print("Liczba Stanów sprawdzonych: ", cnt)
    return result, cnt


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

def main():
    board = []
    data = []
    start1 = time.time()
    board, gen_states1 = board_gen(4, board)
    #print(board)
    result, chck_states1 = capturing(board)
    for el in result:
        if el[0] == 0:
            print(el[1])
    end1 = time.time()
    diff1 = end1 - start1
    print("Czas wykonania: ", diff1)
    data.append([gen_states1, chck_states1, diff1])

    board = []
    start2 = time.time()
    board, gen_states2 = board_gen(5, board)
    #print(board)
    result, chck_states2 = capturing(board)
    for el in result:
        if el[0] == 0:
            print(el[1])
    end2 = time.time()
    diff2 = end2 - start2
    print("Czas wykonania: ", diff2)
    data.append([gen_states2, chck_states2, diff2])

    board = []
    start3 = time.time()
    board, gen_states3 = board_gen(6, board)
    #print(board)
    result, chck_states3 = capturing(board)
    for el in result:
        if el[0] == 0:
            print(el[1])
    end3 = time.time()
    diff3 = end3 - start3
    print("Czas wykonania: ", diff3)
    data.append([gen_states3, chck_states3, diff3])

    board = []
    start4 = time.time()
    board, gen_states4 = board_gen(7, board)
    #print(board)
    result, chck_states4 = capturing(board)
    for el in result:
        if el[0] == 0:
            print(el[1])
    end4 = time.time()
    diff4 = end4 - start4
    print("Czas wykonania: ", diff4)
    data.append([gen_states4, chck_states4, diff4])

    print(data)
    data = np.array(data)
    fig, ax = plt.subplots()
    range = np.arange(len(data))
    ax.bar(x = range, height = data[:,0],width = 0.12,label = "Stany wygenerowane")
    ax.bar(x = range+0.12, height = data[:,1],width = 0.12,label = 'Stany sprawdzone')
    ax.bar(x = range+0.12*2, height = data[:,2]*10000,width = 0.12,label = 'Czas x10000')
    ax.set_xticks(np.arange(len(data)))
    ax.set_xticklabels(["n = 4","n = 5","n = 6","n = 7"])
    ax.legend()
    plt.savefig("Plot.png", format = "png")
    plt.show()

main()