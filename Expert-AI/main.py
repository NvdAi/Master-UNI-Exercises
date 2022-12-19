import numpy as np
# from CHESS import Board


BOARD_SHAPE = (8,8)

kings = [["K",0,6],["k",7,4]]

queens = []

rooks = [["r",0,0]]

bishop = []

knight = []

pawns = [["P",1,7],["P",1,6],["P",1,5]]

nuts_list = [kings, queens, rooks, bishop, knight, pawns]

board = np.zeros(BOARD_SHAPE,dtype=int)
board = board.astype(str)
for item in nuts_list:
    if item == []:
        pass
    else:
        for nut in item :
            print(nut)
            board[nut[1]][nut[2]] = nut[0]

print(board)