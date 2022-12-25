import numpy as np
from itertools import groupby

                                    # start with black nuts
board = np.array([    ['0' , 'b1' , '0' , '0' , 'q' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['0' , '0' , 'p' , '0' , 'K' , '0' , 'r' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , 'p' , '0' , '0'],
                      ['0' , '0' , '0' , 'kn' , 'p' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , 'r' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0']],  dtype=object)
                                    # start with white nuts
print(board)


kingsymbol = ["K","k"]
start_mood = (1,0)  # frist item is black start mood and secend itrm is white start mood (0 is down 1 is top)
check_count = 0 


def check_on_diagonals(board, check_count, symbol, checker_symbols, massage):

    diags = [board[::-1,:].diagonal(i) for i in range(-board.shape[0]+1, board.shape[1])]
    diags.extend(board.diagonal(i) for i in range(board.shape[1]-1,-board.shape[0],-1))
    all_diags = [n.tolist() for n in diags]

    for checker_symbol in checker_symbols:
        for diag in all_diags:

            if (symbol in diag) and (checker_symbol in diag):
                kinx = diag.index(symbol)
                checker_index = diag.index(checker_symbol)

                if kinx > checker_index:
                    if diag[kinx-1]== checker_symbol:
                        print(massage,checker_symbol)
                        check_count +=1 
                    elif groupby(diag[checker_index+1:kinx]) and ("0" in diag[checker_index+1:kinx] ):
                        print(massage,checker_symbol)
                        check_count +=1 
                else:
                    if diag[kinx+1]== checker_symbol:
                        print(massage,checker_symbol)
                        check_count +=1 
                    elif groupby(diag[kinx+1:checker_index]) and ("0" in diag[kinx+1:checker_index] ):
                        print(massage,checker_symbol)
                        check_count +=1 
    return check_count

def check_on_rowcols(board, check_count, symbol, checker_symbol, massage):

    sid = ["on row","on col"]
    for counter,i in  enumerate(sid):  # checking for row and col
        king_indx = np.where(board == symbol)
        row = board[king_indx[0]]
        if counter == 1:
            row = board[: ,king_indx[1]]
            row = np.reshape(board[: ,king_indx[1]],(1,8))

        rook_indx = np.where(row == checker_symbol)
        rook_num = len(rook_indx[1])
        king_indx = np.where(row == symbol)

        if rook_num == 0:
            pass
        elif (rook_num == 1) and (rook_indx[1][0] < king_indx[1][0]):
            if row[king_indx[0][0]][king_indx[1][0]-1] == checker_symbol:
                check_count+=1
                print(massage,i)
            else:
                dist = row[:,rook_indx[1][0]+1 : king_indx[1][0]].flatten()
                ln_dist = len(set(dist))
                if (ln_dist==1) and ("0" in dist):
                    check_count+=1
                    print(massage,i)

        elif (rook_num == 1) and (rook_indx[1][0] > king_indx[1][0]):
            if row[king_indx[0][0]][king_indx[1][0]+1] == checker_symbol:
                check_count+=1
                print(massage,i)
            else:
                dist = row[:,king_indx[1][0]+1 : rook_indx[1][0]].flatten()
                ln_dist = len(set(dist))
                if (ln_dist==1) and ("0" in dist):
                    check_count+=1
                    print(massage,i)

        elif (rook_num == 2) and (max(rook_indx[1]) < king_indx[1][0]):
            if row[king_indx[0][0]][king_indx[1][0]-1] == checker_symbol:
                check_count+=1
                print(massage,i)
            else:
                dist = row[:,max(rook_indx[1])+1 : king_indx[1][0]].flatten()
                ln_dist = len(set(dist))
                if (ln_dist==1) and ("0" in dist):
                    check_count+=1
                    print(massage,i)

        elif (rook_num == 2) and (min(rook_indx[1]) > king_indx[1][0]):
            if row[king_indx[0][0]][king_indx[1][0]+1] == checker_symbol:
                check_count+=1
                print(massage,i)
            else:
                dist = row[:,king_indx[1][0]+1 : min(rook_indx[1])].flatten()
                ln_dist = len(set(dist))
                if (ln_dist==1) and ("0" in dist):
                    check_count+=1
                    print(massage,i)
        
        elif (rook_num == 2) and (min(rook_indx[1]) < king_indx[1][0] < max(rook_indx[1])):
            left = row[:,min(rook_indx[1]) : king_indx[1][0]].flatten()
            ln_left = len(set(left))
            if (ln_left == 1) or (ln_left==2  and "0" in left):
                check_count+=1
                print(massage,i)
            right = row[:,king_indx[1][0] : max(rook_indx[1])].flatten()
            ln_right = len(set(right))
            if (ln_right == 1) or (ln_right==2  and "0" in right):
                check_count+=1
                print(massage,i) 
    return check_count


def is_check_rook(board, check_count, symbol):
    if symbol == "K" :
        rook_symbol = "r"
        massage = "black king checked by white rook "
    else:
        rook_symbol = "R"
        massage = "Wihte king checked by black rook " 
    check_count = check_on_rowcols(board, check_count, symbol, rook_symbol, massage)
    return check_count  

def is_check_pawn(board, check_count, start_mood, symbol ):
    if symbol == "K":
        if start_mood[0] == 1:
            bound = (6,7)
            i,j = (1,1)
        else:
            bound = (0,1)
            i,j = (-1,1)  

        pawn = "p"
        king_color = "black king"
        pawn_color = "white pawn"

    elif symbol == "k":
        if start_mood[1] == 1:
            bound = (6,7)
            i,j = (1,1)
        else:
            bound = (0,1)
            i,j = (-1,1)  
   
        pawn = "P"
        king_color = "white king"
        pawn_color = "black pawn"

    king_indx = np.where(board == symbol)
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

def is_check_knight(board, check_count, symbol):

    if symbol == "K":
        knight_symbol = "kn"
        massage = "Black king checked by white knight"
    else :
        knight_symbol = "KN"
        massage = "White king checked by black knight"


    new_board = np.pad(board, 2)
    king_indx = np.where(new_board == symbol)
    i,j = (king_indx[0][0], king_indx[1][0])

    rectangle_1 = new_board[i-2:i+3 , j-1:j+2]
    rectangle_2 = new_board[i-1:i+2 , j-2:j+3]

    corners_indx = np.ix_((0, -1), (0,-1))
    corners_1 = rectangle_1[corners_indx]
    corners_2 = rectangle_2[corners_indx]
    all_corners = np.concatenate((corners_1, corners_2), axis=0)
    knight_indx = np.where(all_corners == knight_symbol)

    if len(knight_indx[0]) == 0:
        pass
    else:
        print(massage)
        check_count +=1
    return check_count

def is_check_bishop(board, check_count, symbol):
    if symbol == "K" :
        bishop_symbol = ("b1","b2")
        massage = "black king checked by white bishop "
    else:
        bishop_symbol = ("B1","B2")
        massage = "Wihte king checked by black bishop "   
        
    check_count = check_on_diagonals(board, check_count, symbol, bishop_symbol, massage)
    return check_count

def is_check_queen(board, check_count, symbol):
    if symbol == "K" :
        queen_symbol = ("q")
        massage = "black king checked by white queen "
    else:
        queen_symbol = ("Q")
        massage = "white king checked by black queen "  

    check_count = check_on_diagonals(board, check_count, symbol, queen_symbol, massage)
    check_count = check_on_rowcols(board, check_count, symbol, queen_symbol, massage)    
    return check_count


for symbol in kingsymbol:
    print("=======================")
    check_count = is_check_rook(board, check_count, symbol)
    
    check_count = is_check_pawn(board, check_count, start_mood, symbol)
    
    check_count = is_check_knight(board, check_count, symbol)
    
    check_count = is_check_bishop(board, check_count, symbol)
    
    check_count = is_check_queen(board, check_count, symbol)

    print(check_count)
    check_count=0
    qq
