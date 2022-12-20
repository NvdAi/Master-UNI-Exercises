import numpy as np
# from CHESS import Board

BOARD_SHAPE = (8,8)

kings = [["K",0,6],["k",7,4]]

queens = []

rooks = [["r",0,1]]

bishop = [["b",0,5]]

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
            board[nut[1]][nut[2]] = nut[0]

print(board)

# different checks that should be check  
    # check by rook   on rows and cols
    # check by queen  on rows and cols and diameters
    # check by bishop on diameters
    # check by knight on a L 
    # check by pawn   on diameters; if distance ==1

check_count = 0 
king_indx = np.where(board == "K")
# print(king_indx)

def is_check_rook(board, king_indx, check_count):
    row = board[king_indx[0]]
    col = board[: ,king_indx[1]]
    rook_indx = np.where(row == "r")

    L = len(rook_indx[0])
    if  L == 0:
        print("we dont have rook ")

    elif L == 1 and king_indx[1][0] < rook_indx[1][0]:
        print("rook in right")
        dist = row[:,king_indx[1][0] : rook_indx[1][0]]
        ln = len(set(dist.flatten()))
        if (ln == 1) or  (ln == 2):
            print("WE HAVE CHECK By ROOK ")

    elif L == 1 and rook_indx[1][0] < king_indx[1][0]:
        print("rook in left")
        dist = row[:,rook_indx[1][0] : king_indx[1][0]]
        ln = len(set(dist.flatten()))
        if (ln == 1) or  (ln == 2):
            print("WE HAVE CHECK By ROOK ")



    # check by rook 






is_check_rook(board, king_indx, check_count)