board = []
result = []
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
                board = check_captures(board)
        if len(board) == 0:
                    break
    if len(board) != 0:
        result.append(board[-1][0])
        del board[-1]
        return DFS(n, board, result)
    else:
        return result, counter
        
def check_captures(board):
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

board_1, counter = DFS(4,board,result)
print(board_1, "\nLiczba stanów wygenerowanych:", counter)
