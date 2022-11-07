import numpy as np
import matplotlib.pyplot as plt
import time


def Best_First_Search_H1(n, board):
    close = []
    cnt1 = 0
    cnt2 = 0
    w_row = np.array([n - (int(board[idx]) + 1) + 1 if idx < n/2 else int(board[idx]) + 1 for idx in range(len(board))])
    h1 = ((n - 1) * w_row)
    open = [el for el in board]

    while len(open) > 0:
        min_idx = np.array(np.where(h1 == min(h1))).flatten() 
        pos = open[min_idx[0]]
        del open[min_idx[0]]
        h1 = np.delete(h1, min_idx[0])

####
        if len(pos) == n:
            if is_valid(pos) == True:
                cnt2 +=1
                return pos, cnt1, cnt2
            else:
                cnt1+=1
                cnt2+=1
                continue

        elif is_valid(pos) == False:
            cnt1+=1
            continue
####
        else:
            t = []
            for i in range(n):
                t.append([''.join(pos) + str(i)])

        for el in t: 
            cnt1+=1
            if el in close:
                continue
            else:
                sum = 0
                for e in el[0]:
                    sum += w_row[int(e)]
                h = (n - len(el[0])) * sum

            if el[0] not in open:
                open.append(el[0])
                h1 = np.append(h1, h)
            else:
                if h < min(h1):
                    open[open.index(el[0])] = el[0]
        
        close.append(pos)
    return 0

def Best_First_Search_H2(n, board):
    close = []
    cnt1 = 0
    cnt2 = 0
    open = [el for el in board]
    h1 = np.array([h2_counter(el) for el in open])

    while len(open) > 0:
        min_idx = np.array(np.where(h1 == min(h1))).flatten()
        pos = open[min_idx[0]]
        del open[min_idx[0]]
        h1 = np.delete(h1, min_idx[0])

####
        if len(pos) == n:
            if is_valid(pos) == True:
                cnt2 +=1
                return pos, cnt1, cnt2
            else:
                cnt1+=1
                cnt2+=1
                continue

        elif is_valid(pos) == False:
            cnt1+=1
            continue
####

        else:
            t = []
            for i in range(n):
                t.append([''.join(pos) + str(i)])

        for el in t: 
            cnt1+=1
            if el in close:
                continue
            h = h2_counter(el[0])
            

            if el[0] not in open:
                open.append(el[0])
                h1 = np.append(h1, h)
            else:
                if h < min(h1):
                    open[open.index(el[0])] = el[0]
        close.append(pos)
    return 0

def Best_First_Search_H3(n, board):
    close = []
    cnt1 = 0
    cnt2 = 0
    S = (n / 2)*(n - 1)
    open = [el for el in board]
    dn = np.array([dn_counter(el) for el in open])
    h1 = S - dn

    while len(open) > 0:
        min_idx = np.array(np.where(h1 == min(h1))).flatten() 
        pos = open[min_idx[0]]
        del open[min_idx[0]]
        h1 = np.delete(h1, min_idx[0])
        
####
        if len(pos) == n:
            if is_valid(pos) == True:
                cnt2+=1
                return pos, cnt1, cnt2
            else:
                cnt1+=1
                cnt2+=1
                continue

        elif is_valid(pos) == False:
            cnt1+=1
            continue

####
        else:
            t = []
            for i in range(n):
                t.append([''.join(pos) + str(i)])

        for el in t: 
            cnt1+=1
            if el in close:
                continue

            dn = dn_counter(el[0])
            h = S - dn
            
            if el[0] not in open:
                open.append(el[0])
                h1 = np.append(h1, h)
            else:
                if h < min(h1):
                    open[open.index(el[0])] = el[0]
        
        close.append(pos)
    return 0

def dn_counter(pos):
    temp = []
    cnt = 0
    for el in pos:
        if el not in temp:
            temp.append(el)
            cnt += 1
        else: continue
    return cnt

def h2_counter(pos):
    cnt = 0
    for idx, el in enumerate(pos):
        for idx1, el1 in enumerate(pos):
            if idx1 > idx:
                if attack(el, idx, el1, idx1) == True:
                    cnt += 1
                else:
                    continue
            else:
                continue
    return cnt

def is_valid(pos):
    for idx, el in enumerate(pos):
        for idx1, el1 in enumerate(pos):
            if idx1 > idx:
                if attack(el, idx, el1, idx1) == True:
                    return False
                else:
                    continue
            else:
                continue
    return True
    
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

n = 9
board = [str(i) for i in range(n)]

print(Best_First_Search_H1(n, board))

def Heurestic_Comparision(x, y):
    data_H1 = []
    data_H2 = []
    data_H3 = []
    for n in range(x,y):

        board = [str(i) for i in range(n)]
        result = []

        start1 = time.time()
        board_1, counter, counter1 = Best_First_Search_H1(n,board)
        print("\nH1 n:",n,"\nWynik:", board_1, "\nLiczba stanów wygenerowanych:", counter, "\nLiczba stanów sprawdzonych:", counter1)
        end1 = time.time()
        print("Czas wykonania:", end1 - start1)
        data_H1.append([counter, counter1, end1-start1])

        board = [str(i) for i in range(n)]
        result = []

        start1 = time.time()
        board_1, counter, counter1 = Best_First_Search_H2(n,board)
        print("\nH2 n:",n,"\nWynik:", board_1, "\nLiczba stanów wygenerowanych:", counter, "\nLiczba stanów sprawdzonych:", counter1)
        end1 = time.time()
        print("Czas wykonania:", end1 - start1)
        data_H2.append([counter, counter1, end1-start1])

        board = [str(i) for i in range(n)]
        result = []

        start1 = time.time()
        board_1, counter, counter1 = Best_First_Search_H3(n, board)
        print("\nH3 n:",n,"\nWynik:", board_1, "\nLiczba stanów wygenerowanych:", counter, "\nLiczba stanów sprawdzonych:", counter1)
        end1 = time.time()
        print("Czas wykonania:", end1 - start1)
        data_H3.append([counter, counter1, end1-start1])

    data_H1 = np.array(data_H1)
    fig, ax = plt.subplots(3)
    range1 = np.arange(len(data_H1))
    ax[0].bar(x = range1, height = data_H1[:,0],width = 0.12,label = "Stany wygenerowane")
    ax[0].bar(x = range1+0.12, height = data_H1[:,1],width = 0.12,label = 'Stany sprawdzone')
    ax[0].bar(x = range1+0.24, height = data_H1[:,2]*1000,width = 0.12,label = 'Czas x10000')
    ax[0].set_xticks(np.arange(len(data_H1)))
    ax[0].set_xticklabels(["n = " + str(j) for j in range(x,y)])
    ax[0].legend()
    ax[0].set_title("H1")

    data_H2 = np.array(data_H2)
    range1 = np.arange(len(data_H2))
    ax[1].bar(x = range1, height = data_H2[:,0],width = 0.12,label = "Stany wygenerowane")
    ax[1].bar(x = range1+0.12, height = data_H2[:,1],width = 0.12,label = 'Stany sprawdzone')
    ax[1].bar(x = range1+0.24, height = data_H2[:,2]*1000,width = 0.12,label = 'Czas x10000')
    ax[1].set_xticks(np.arange(len(data_H2)))
    ax[1].set_xticklabels(["n = " + str(j) for j in range(x,y)])
    ax[1].legend()
    ax[1].set_title("H2")

    data_H3 = np.array(data_H3)
    range1 = np.arange(len(data_H3))
    ax[2].bar(x = range1, height = data_H3[:,0],width = 0.12,label = "Stany wygenerowane")
    ax[2].bar(x = range1+0.12, height = data_H3[:,1],width = 0.12,label = 'Stany sprawdzone')
    ax[2].bar(x = range1+0.24, height = data_H3[:,2]*1000,width = 0.12,label = 'Czas x10000')
    ax[2].set_xticks(np.arange(len(data_H3)))
    ax[2].set_xticklabels(["n = " + str(j) for j in range(x,y)])
    ax[2].legend()
    ax[2].set_title("H3")
    plt.savefig("Plot.png", format = "png")
    plt.show()

Heurestic_Comparision(4, 10)