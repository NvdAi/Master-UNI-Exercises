import numpy as np
# from CHESS import Board

# BOARD_SHAPE = (8,8)

# kings = [["K",3,6],["k",7,4]]

# queens = []

# rooks = [["r",0,0],["r",0,6],["r",3,7],["r",3,1],["r",7,6]]

# bishop = [["b",3,4]]

# knight = []

# pawns = [["P",1,6],["P",1,0],["P",1,5]]

# nuts_list = [kings, queens, rooks, bishop, knight, pawns]

# board = np.zeros(BOARD_SHAPE,dtype=int)
# board = board.astype(str)
# for item in nuts_list:
#     if item == []:
#         pass
#     else:
#         for nut in item :
#             board[nut[1]][nut[2]] = nut[0]

                                    # stat with black nuts
board = np.array([    ['0' , 'p' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['K' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , 'P' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , 'k'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0']],  dtype=object)
                                    # stat with white nuts
print(board)

# different checks that should be check  
    # check by rook   on rows and cols
    # check by queen  on rows and cols and diameters
    # check by bishop on diameters
    # check by knight on a L 
    # check by pawn   on diameters; if distance ==1

check_count = 0 

def is_check_rook(board, check_count):

    for i in range(2):
        print("===========",i,"==================")
        king_indx = np.where(board == "K")
        row = board[king_indx[0]]

        if i==1:
            row = board[: ,king_indx[1]]
            row = np.reshape(board[: ,king_indx[1]],(1,8))
        # print(row)
        rook_indx = np.where(row == "r")
        king_indx = np.where(row == "K")
        L = len(rook_indx[0])
        if  L == 0:
            print("we dont have rook ")

        elif L == 1 and king_indx[1][0] < rook_indx[1][0]:
            print("rook in right")
            dist = row[:,king_indx[1][0] : rook_indx[1][0]]
            s = list(set(dist.flatten()))
            ln = len(set(dist.flatten()))
            if (ln == 1) or  ( (ln == 2) and (s == ["0","K"])) or ((ln == 2) and (s == ["K","0"])):
                print("WE HAVE CHECK By ROOK ")
                check_count +=1
                return check_count
                break

        elif L == 1 and rook_indx[1][0] < king_indx[1][0]:
            print("rook in left")
            dist = row[:,rook_indx[1][0] : king_indx[1][0]]
            s = list(set(dist.flatten()))
            ln = len(set(dist.flatten()))
            if (ln == 1) or ( (ln == 2) and (s == ["0","r"])) or ((ln == 2) and (s == ["r","0"])) :
                print("WE HAVE CHECK By ROOK ")
                check_count +=1
                break

        elif (L==2 ) and (max(rook_indx[1]) <  king_indx[1][0]):
            print("we have tow rook in left")
            dist = row[:,rook_indx[1][1] : king_indx[1][0]]
            ln = len(set(dist.flatten()))
            s = list(set(dist.flatten()))
            if (ln == 1) or ( (ln == 2) and (s == ["0","r"])) or ((ln == 2) and (s == ["r","0"])):
                print("WE HAVE CHECK By closer ROOK ")
                check_count +=1
                break

        elif (L==2) and (king_indx[1][0] < min(rook_indx[1])) :
            print("we have tow rook in right")
            dist = row[:,king_indx[1][0] : rook_indx[1][0]]
            s = list(set(dist.flatten()))
            ln = len(set(dist.flatten()))
            if (ln == 1) or  ( (ln == 2) and (s == ["0","K"])) or ((ln == 2) and (s == ["K","0"])):
                print("WE HAVE CHECK By ROOK ")
                check_count +=1
                break

        elif (L==2) and (min(rook_indx[1]) < king_indx[1][0] < max(rook_indx[1])) :
            print("we have two rook left and right")
            dist = row[:,rook_indx[1][0] : king_indx[1][0]]
            s = list(set(dist.flatten())) 
            ln = len(set(dist.flatten()))
            if (ln == 1) or  ( (ln == 2) and (s == ["0","r"])) or ((ln == 2) and (s == ["r","0"])):
                print("WE HAVE CHECK By  left ROOK ")
                check_count +=1
                break

            dist = row[:, king_indx[1][0]:rook_indx[1][1]]
            s = list(set(dist.flatten()))    
            ln = len(set(dist.flatten()))
            if (ln == 1) or  ( (ln == 2) and (s == ["0","K"])) or ((ln == 2) and (s == ["K","0"])) :
                print("WE HAVE CHECK By right ROOK")
                check_count +=1
                break


def is_check_pawn(board, check_count,B_OR_W ):
    if B_OR_W == "K":
        bound = (6,7)
        i,j = (1,1)
        pawn = "p"
        king_color = "black king"
        pawn_color = "white pawn"
    elif B_OR_W == "k":
        bound = (0,1)
        i,j = (-1,1)
        pawn = "P"
        king_color = "white king"
        pawn_color = "black pawn"

    king_indx = np.where(board == B_OR_W)
    king_row, king_col = king_indx[0][0],king_indx[1][0]
    # black king in white start region
    if (king_row == bound[0]) or (king_row == bound[1]):
        print(king_color ," is in opponent's starting area ")
    # black king in saids (col 0)
    elif (king_col == 1)  and (board[king_row +i][king_col +j] == pawn):
        print(king_color, "checked by",pawn_color)
        check_count += 1
    # black king in saids (col 7)
    elif (king_col == 7)  and (board[king_row +i][king_col -j] == pawn):
        print(king_color, "checked by",pawn_color)
        check_count += 1    
    # black king in other locations
    elif (board[king_row +i][king_col +j] == pawn) or (board[king_row +i][king_col -j] == pawn):
        print(king_color, "checked by",pawn_color)
        check_count += 1
    else:
        print(king_color ," dont have check by ", pawn_color )
    return check_count


# check_count = is_check_rook(board, check_count)

check_count = is_check_pawn(board, check_count,"K")
print("=================================")
check_count = is_check_pawn(board, check_count,"k")