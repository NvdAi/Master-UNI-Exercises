import numpy as np
from itertools import groupby

                                    # start with black nuts
board = np.array([    ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['0' , 'r7' , 'p' , '0' , 'r5' , 'p' , 'r3' , 'K'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0'],
                      ['0' , '0' , '0' , '0' , '0' , '0' , '0' , '0']],  dtype=object)
                                    # start with white nuts
print(board)


kingsymbol = ["K","k"]
start_mood = (1,0)  # frist item is black start mood and secend itrm is white start mood (0 is down 1 is top)
check_count = 0 

def check_on_rowcols(board, check_count, symbol, checker_symbols, massage):
    king_indx = np.where(board == symbol)
    row = board[king_indx[0]]
    col = board[:,king_indx[1]]
    col = np.reshape(board[: ,king_indx[1]],(1,8))
    cheched_by = 0

    side = [(row[0], "on row by "),(col[0],"on col by")]
    for i,j in side:
        check_list = []
        for item in i:
            if item == "0":
                pass
            else:
                check_list.append(item)

        intersection = list(set(check_list) & set(checker_symbols))

        if len(intersection) > 0:
            kindx = check_list.index(symbol)
            if (kindx == 0) and (check_list[kindx+1] in checker_symbols):
                check_count+=1
                cheched_by = check_list[kindx+1]
                print(massage,j,cheched_by)
                break
            elif (kindx == len(check_list)-1) and (check_list[kindx-1] in checker_symbols):
                check_count+=1
                cheched_by = check_list[kindx-1]
                print(massage,j,cheched_by)
                break
            elif check_list[kindx+1] in checker_symbols:
                check_count+=1
                cheched_by = check_list[kindx+1]
                print(massage,j,cheched_by)
                break
            elif check_list[kindx-1] in checker_symbols:
                check_count+=1
                cheched_by = check_list[kindx-1]
                print(massage,j,cheched_by)
                break
            else:
                pass
        else:
            print("we dont have rook",j)
    return check_count, cheched_by
 

def is_check_rook(board, check_count, symbol):
    if symbol == "K" :
        checker_symbols = ["r1","r2","r3","r4","r5","r6","r7","r8","r9","r10"]
        massage = "black king checked by white rook "

    else:
        checker_symbols = ["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10"]
        massage = "Wihte king checked by black rook " 

    check_count, checked_by = check_on_rowcols(board, check_count, symbol, checker_symbols, massage)
    return check_count, checked_by  



for symbol in kingsymbol:
    check_count = is_check_rook(board, check_count, symbol)
    check_count_all = check_count
    qq
    
