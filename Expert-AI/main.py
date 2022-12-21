import numpy as np


                                    # stat with black nuts
board = np.array([    ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['K' , '0' , '0' , '0' , '0' , '0' , 'R' , '0'],
                      ['0' , 'p' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['r' , '0' , '0' , '0' , '0' , '0' , 'k' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
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

kingsymbol = ["K","k"]
start_mood = (1,0)  # frist item is black start mood and secend itrm is white start mood (0 is down 1 is top)
check_count = 0 

def is_check_rook(board, check_count, symbol):

    sid = ["row","column"]
    for counter,i in  enumerate(sid):  # checking for row and col
        king_indx = np.where(board == symbol)
        row = board[king_indx[0]]

        if counter==1:
            row = board[: ,king_indx[1]]
            row = np.reshape(board[: ,king_indx[1]],(1,8))

        if symbol == "K":
            rook_symbol = "r"
        else:
            rook_symbol = "R"

        rook_indx = np.where(row == rook_symbol )
        king_indx = np.where(row == symbol)

        L = len(rook_indx[0])
        if  L == 0:
            print("we dont have rook in",i)

        elif L == 1 and king_indx[1][0] < rook_indx[1][0]:
            # print("rook in right on ",i)
            dist = row[:,king_indx[1][0] : rook_indx[1][0]]
            s = list(set(dist.flatten()))
            ln = len(set(dist.flatten()))

            if (ln == 1) or  ( (ln == 2) and (s == ["0",symbol])) or ((ln == 2) and (s == [symbol,"0"])):
                print("WE HAVE CHECK By ROOK on",i)
                check_count +=1
                

        elif L == 1 and rook_indx[1][0] < king_indx[1][0]:
            # print("rook in left on",i)
            dist = row[:,rook_indx[1][0] : king_indx[1][0]]
            s = list(set(dist.flatten()))
            ln = len(set(dist.flatten()))
            if (ln == 1) or ( (ln == 2) and (s == ["0",rook_symbol])) or ((ln == 2) and (s == [rook_symbol,"0"])) :
                print("WE HAVE CHECK By ROOK on",i)
                check_count +=1
                

        elif (L==2 ) and (max(rook_indx[1]) <  king_indx[1][0]):
            # print("we have tow rook in left on ",i)
            dist = row[:,rook_indx[1][1] : king_indx[1][0]]
            ln = len(set(dist.flatten()))
            s = list(set(dist.flatten()))
            if (ln == 1) or ( (ln == 2) and (s == ["0", rook_symbol ])) or ((ln == 2) and (s == [rook_symbol,"0"])):
                print("WE HAVE CHECK By closer ROOK on ",i)
                check_count +=1


        elif (L==2) and (king_indx[1][0] < min(rook_indx[1])) :
            # print("we have tow rook in right on",i)
            dist = row[:,king_indx[1][0] : rook_indx[1][0]]
            s = list(set(dist.flatten()))
            ln = len(set(dist.flatten()))
            if (ln == 1) or  ( (ln == 2) and (s == ["0",symbol])) or ((ln == 2) and (s == [symbol,"0"])):
                print("WE HAVE CHECK By ROOK on",i)
                check_count +=1

        elif (L==2) and (min(rook_indx[1]) < king_indx[1][0] < max(rook_indx[1])) :
            # print("we have two rook left and right on",i)
            dist = row[:,rook_indx[1][0] : king_indx[1][0]]
            s = list(set(dist.flatten())) 
            ln = len(set(dist.flatten()))
            if (ln == 1) or  ( (ln == 2) and (s == ["0",rook_symbol])) or ((ln == 2) and (s == [rook_symbol,"0"])):
                print("WE HAVE CHECK By  left ROOK on",i)
                check_count +=1

            dist = row[:, king_indx[1][0]:rook_indx[1][1]]
            s = list(set(dist.flatten()))    
            ln = len(set(dist.flatten()))
            if (ln == 1) or  ( (ln == 2) and (s == ["0",symbol])) or ((ln == 2) and (s == [symbol,"0"])) :
                print("WE HAVE CHECK By right ROOK on",i)
                check_count +=1
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

for symbol in kingsymbol:
    print("is check on",symbol)
    check_count = is_check_rook(board, check_count, symbol)

    check_count = is_check_pawn(board, check_count, start_mood, symbol)
    print(check_count)
    check_count=0
