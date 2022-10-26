board = []
result = []
###inteligentne - sprawdzanie bic zawsze
def board_gen(n, board, result):
    '''Board Generation using DFS'''
    #counter = 0
    if len(board) == 0:
        for i in range(n):
            board.append([str(i)])
            #counter += 1
    while len(board[-1][0]) < n:
        last_el = board[-1] 
        del board[-1]
        for i in range(n):
            #counter += 1
            board.append([''.join(last_el) + str(i)])
            if (len(board[-1][0]) == n):
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
        if len(board) == 0:
                    break
    if len(board) != 0:
        result.append(board[-1][0])
        del board[-1]
        return board_gen(n, board, result)
    else:
        return result
        
    #print("Liczba stanów wygenerowanych: ", counter)
    #return board, counter

def capturing(board):
    '''Captures in every position'''
    #cnt = 0
    result = []
    for pos in board:
        score = 0
        #cnt += 1
        for idx, el in enumerate(pos[0]):
            for idx1, el1 in enumerate(pos[0]):
                if idx1 > idx:
                    if attack(el, idx, el1, idx1) == True:
                        score += 1
        result.append([score, pos])
    #print("Liczba Stanów sprawdzonych: ", cnt)
    return result


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

print(board_gen(4,board,result))