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




def main():
    run = True
    turn = PLAYER1

    # loop of the game
    while run:
        if turn == PLAYER1:
            val = input("Player 1")
            place(board, int(val), PLAYER1+1)
            reprint(board)
        else:
            val = input("Player 2")
            place(board, int(val), PLAYER2 + 1)
            reprint(board)

        turn = turn + 1
        turn = turn % 2


board = create_board()
print(board)
main()
