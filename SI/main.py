n = 4
board = []

def board_gen(n, board):
    if len(board) == 0:
        for i in range(n):
            board.append([str(i)])
    elif len(board[0][0]) == 4:
        return board    
    else:
        for i in range(4):
            board.append([''.join(board[0]) + str(i)])
        del board[0]
    return board_gen(n, board)
    
def capturing(board):
    """TODO"""
    score_tab = []
    score = 0
    for pos in board:
        for i in range(len(pos)):
            if pos[-i] == pos[i]:
                score += 1
        score_tab.append(score)
        score = 0
    return score

print(board_gen(n, board))
print(capturing(board))
