# connectFour.py

import numpy as py

ROW = 6
COL = 7
PLAYER1 = 0
PLAYER2 = 1
# create a empty board
def create_board():
    return py.zeros((ROW, COL))

def place(board, col, player):
    for i in range(ROW):
        if board[i][col] == 0:
            board[i][col] = player
            break

def reprint(board):
    print(py.flip(board, 0))

def full_col(board, col):
    if board[ROW-1][col] == 0:
        return False
    else:
        return True

# check whether this player won the game
def win(board, player):
    pass
    # check vertical
    for row in range(ROW-3):
        for col in range(COL):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True

    # check horizontal
    for col in range(COL-3):
        for row in range(ROW):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True

    # check positively slope diagonals

    # check negatively slope diagonals




def main():
    run = True
    turn = PLAYER1

    # loop of the game
    while run:
        # player 1
        if turn == PLAYER1:
            val = int(input("Player 1"))
            if full_col(board, val) is False:
                place(board, val, PLAYER1+1)
                reprint(board)



        # player 2
        else:
            val = int(input("Player 1"))
            if full_col(board, val) is False:
                place(board, val, PLAYER2 + 1)
                reprint(board)

        turn = turn + 1
        turn = turn % 2


board = create_board()
print(board)
main()
