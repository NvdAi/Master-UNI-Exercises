import numpy as np

black_symbols = ["KN1","KN2","KN3","KN4","KN5","KN6","KN7","KN8","KN9","KN10","P1","P2","P3","P4","P5","P6","P7","P8","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9"]
white_symbols = ["kn1","kn2","kn3","kn4","kn5","kn6","kn7","kn8","kn9","kn10","p1","p2","p3","p4","p5","p6","p7","p8","b1","b2","b3","b4","b5","b6","b7","b8","b9","b10","r1","r2","r3","r4","r5","r6","r7","r8","r9","r10","q1","q2","q3","q4","q5","q6","q7","q8","q9"]
                                    # start with black nuts
board = np.array([    ['0'  ,  'p1'  ,  'q2'  ,  'kn4'  ,  '0'  ,  '0'  ,  '0'  ,  '0'],
                      ['0'  ,  'P4'  ,  'k'  ,  'b3'  ,  '0'  ,  '0'  ,  '0'  ,  '0'],
                      ['B1'  ,  'kn2'  ,  'b7'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'],
                      ['0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'],
                      ['0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'],
                      ['0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  'Q3'  ,  '0'],
                      ['0'  ,  'K'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'],
                      ['0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  '0'  ,  '0']],  dtype=object)
                                    # start with white nuts

def check_on_diagonals(board, symbol, checker_symbols, massage):
    diags = [board[::-1,:].diagonal(i) for i in range(-board.shape[0]+1, board.shape[1])]
    diags.extend(board.diagonal(i) for i in range(board.shape[1]-1,-board.shape[0],-1))
    all_diags = [n.tolist() for n in diags]
    checked_by = 0
    for diag in all_diags:
        check_list = [-1]
        if (symbol in diag) and len(list(set(diag) & set(checker_symbols)))>0:
            for item in diag:
                if item == "0":
                    pass
                else:
                    check_list.append(item)
                    look = (check_list[-2],check_list[-1])
                    if (look[0] in checker_symbols) and (look[1] == symbol):
                        checked_by = look[0]
                        # print(massage,checked_by)
                        break 
                    elif (look[1] in checker_symbols) and (look[0] == symbol):                  
                        checked_by = look[1]
                        # print(massage,checked_by)
                        break
                    else:
                        pass
        elif checked_by != 0:
            break
        else:
            pass 
    return checked_by
  
def check_on_rowcols(board, symbol, checker_symbols, massage):
    king_indx = np.where(board == symbol)
    row = board[king_indx[0]]
    col = board[:,king_indx[1]]
    col = np.reshape(col,(1,8))

    checked_by = 0
    side = [(row[0], "on row by "),(col[0],"on col by")]

    for i,j in side:
        check_list = [-1]
        for item in i:
            
            if item == "0":
                pass
            else:
                check_list.append(item)
                look = (check_list[-2],check_list[-1])
                if (look[0] in checker_symbols) and (look[1] == symbol):
                    checked_by = look[0]
                    # print(massage,j,checked_by)
                    break 
                elif (look[1] in checker_symbols) and (look[0] == symbol):                  
                    checked_by = look[1]
                    # print(massage,j,checked_by)
                    break
                else:
                    pass
        
        if checked_by != 0:
            break
    return  checked_by

def is_check_queen(board, symbol):
    if symbol == "K" :
        checker_symbols = ["q1","q2","q3","q4","q5","q6","q7","q8","q9"]
        massage = "black king checked by white queen "
    else:
        checker_symbols = ["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9"]
        massage = "white king checked by black queen "  
    checked_by = check_on_rowcols(board, symbol, checker_symbols, massage) 
    if checked_by == 0:
        checked_by = check_on_diagonals(board, symbol, checker_symbols, massage)   
    return checked_by

def is_check_rook(board, symbol):
    if symbol == "K" :
        checker_symbols = ["r1","r2","r3","r4","r5","r6","r7","r8","r9","r10"]
        massage = "black king checked by white rook "
    else:
        checker_symbols = ["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10"]
        massage = "Wihte king checked by black rook " 
    checked_by = check_on_rowcols(board, symbol, checker_symbols, massage)
    return  checked_by  

def is_check_bishop(board, symbol):
    if symbol == "K" :
        checker_symbols = ("b1","b2","b3","b4","b5","b6","b7","b8","b9","b10")
        massage = "black king checked by white bishop "
    else:
        checker_symbols = ("B1","B2","B3","B4","B5","B6","B7","B8","B9","B10")
        massage = "Wihte king checked by black bishop "      
    checked_by = check_on_diagonals(board, symbol, checker_symbols, massage)
    return checked_by

def is_check_knight(board, symbol):
    if symbol == "K":
        checker_symbols = ["kn1","kn2","kn3","kn4","kn5","kn6","kn7","kn8","kn9","kn10"]
        massage = "Black king checked by white knight"
    else :
        checker_symbols = ["KN1","KN2","KN3","KN4","KN5","KN6","KN7","KN8","KN9","KN10"]
        massage = "White king checked by black knight"
    chekecd_by = 0
    new_board = np.pad(board, 2)
    king_indx = np.where(new_board == symbol)
    i,j = (king_indx[0][0], king_indx[1][0])

    rectangle_1 = new_board[i-2:i+3 , j-1:j+2]
    rectangle_2 = new_board[i-1:i+2 , j-2:j+3]

    corners_indx = np.ix_((0, -1), (0,-1))
    corners_1 = rectangle_1[corners_indx]
    corners_2 = rectangle_2[corners_indx]
    all_corners = np.concatenate((corners_1, corners_2), axis=0)

    intersection = list (set ( all_corners.flatten() ) & set(checker_symbols))
    if len(intersection) > 0:
        # print(massage,intersection[0])
        chekecd_by = intersection[0]
    else:
        pass 
    return chekecd_by

def is_check_pawn(board, symbol, start_mood):
    new_board = np.pad(board,((0,0),(1,1)))
    king_indx = np.where(new_board == symbol)
    king_row, king_col = king_indx[0][0],king_indx[1][0]
    checked_by = 0

    if (symbol == "K")  and  (start_mood[0] == 1):
        checker_symbols = ["p1","p2","p3","p4","p5","p6","p7","p8"]
        massage = "Black king checked by white pawn"
        LD = new_board[king_row+1][king_col-1]
        RD = new_board[king_row+1][king_col+1]
        if LD in checker_symbols:
            checked_by = LD
            # print(massage,LD)
        elif RD in checker_symbols:
            checked_by = RD
            # print(massage,RD)
        else:
            pass

    elif (symbol == "K")  and  (start_mood[0] == 0):
        checker_symbols = ["p1","p2","p3","p4","p5","p6","p7","p8"]
        massage = "Black king checked by white pawn by"
        LU = new_board[king_row-1][king_col-1]
        RU = new_board[king_row-1][king_col+1]
        if LU in checker_symbols:
            checked_by = LU
            # print(massage,LU)
        elif RU in checker_symbols:
            checked_by = RU
            # print(massage,RU)
        else:
            pass
    
    elif (symbol == "k")  and  (start_mood[0] == 1):
        checker_symbols = ["P1","P2","P3","P4","P5","P6","P7","P8"]
        massage = "White king checked by black pawn by"   
        LD = new_board[king_row+1][king_col-1]
        RD = new_board[king_row+1][king_col+1]
        if LD in checker_symbols:
            checked_by = LD
            # print(massage,LD)
        elif RD in checker_symbols:
            checked_by = RD
            # print(massage,RD)
        else:
            pass
    
    elif (symbol == "k")  and  (start_mood[0] == 1):
        checker_symbols = ["p1","p2","p3","p4","p5","p6","p7","p8"]
        massage = "Black king checked by white pawn by"
        LU = new_board[king_row-1][king_col-1]
        RU = new_board[king_row-1][king_col+1]
        if LU in checker_symbols:
            checked_by = LU
            # print(massage,LU)
        elif RU in checker_symbols:
            checked_by = RU
            # print(massage,RU)
        else:
            pass       
    return checked_by    

def check_checker(board, symbol,start_mood):
    checkers_list = []
    checked_by = is_check_queen(board, symbol)
    if checked_by !=0:
        checkers_list.append(checked_by)
    
    checked_by = is_check_rook(board, symbol)
    if checked_by !=0:
        checkers_list.append(checked_by)
        if len(checkers_list)==2:
            checkers_list.append(symbol)
            return checkers_list
            

    checked_by = is_check_bishop(board, symbol)
    if checked_by !=0:
        checkers_list.append(checked_by)
        if len(checkers_list)==2:
            checkers_list.append(symbol)
            return checkers_list
           
    checked_by = is_check_knight(board, symbol)
    if checked_by !=0:
        checkers_list.append(checked_by)
        if len(checkers_list)==2:
            checkers_list.append(symbol)
            return checkers_list
            

    checked_by = is_check_pawn(board, symbol, start_mood)
    if checked_by !=0:
        checkers_list.append(checked_by)
        if len(checkers_list)==2:
            checkers_list.append(symbol)
            return checkers_list  
    return checkers_list

#we have 3 ways to prefer of check #1 run king  #2 fight with checker nut #3 put a nut between king and checker nut

def fight(board, checkers_list, all_symbols, start_mood, opponent_king):
    checker = checkers_list[0]
    checker_index = np.where(board == checker)
    opponent_king_index =  np.where(board == opponent_king)
    board[checker_index[0][0]][checker_index[1][0]] = opponent_king
    board[opponent_king_index[0][0]][opponent_king_index[1][0]] = checker
    test = check_checker(board,opponent_king,start_mood)
    if len(test) > 0:
        return True
    else:
        board[checker_index[0][0]][checker_index[1][0]] = checker 
        board[opponent_king_index[0][0]][opponent_king_index[1][0]] = opponent_king      
        return False

def defense(board, checkers_list, all_symbols, start_mood,opponent_king):
    checked_king = checkers_list[-1]
    checker = checkers_list[0]
    checked_king_index = np.where(board == checked_king)
    checker_index = np.where(board == checker)
    opponent_king_index = np.where(board == opponent_king)
    kindx = (checked_king_index[0][0],checked_king_index[1][0])
    
    if kindx[0] == checker_index[0][0]:
        t=True
        if kindx[1] < checker_index[1][0]:
            distance  = board[kindx[0], kindx[1]+1 : checker_index[1][0]]
            mover = kindx[1]
        else:
            distance  = board[kindx[0],  checker_index[1][0]+1 : kindx[1]]
            mover = checker_index[1][0]
    elif kindx[1] == checker_index[1][0]:
        t=True
        if kindx[0] < checker_index[0][0]:
            distance  = board[kindx[0] : checker_index[0][0], kindx[1]]
            mover = kindx[0]
        else:
            distance  = board[checker_index[0][0] : kindx[0] , kindx[1]]
            mover = checker_index[0][0]
    else:
        new_board = np.pad(board,1)
        checked_king_index = np.where(new_board == checked_king)
        kindx = (checked_king_index[0][0],checked_king_index[1][0])
        free_loc = ((kindx[0]-1,kindx[1]-1),(kindx[0]-1,kindx[1]+1),(kindx[0]+1,kindx[1]-1),(kindx[0]+1,kindx[1]+1))

        mover_indx = 0
        for item in free_loc:
            if  new_board[item] == "0":
                mover_indx = free_loc.index(item)
            elif new_board[item] == checker:
                return False
            else:
                pass 

        new_board = new_board[1:9 , 1:9]
        checked_king_index = np.where(new_board == checked_king)
        kindx = (checked_king_index[0][0],checked_king_index[1][0])
        free_loc = ((kindx[0]-1,kindx[1]-1),(kindx[0]-1,kindx[1]+1),(kindx[0]+1,kindx[1]-1),(kindx[0]+1,kindx[1]+1))
        mover = free_loc[mover_indx]
    
        next_loc = "0"    
        while (next_loc == "0"):
            new_board[mover[0]][mover[1]] = opponent_king
            new_board[opponent_king_index[0][0]][opponent_king_index[1][0]] = "0"
            test =  check_checker(new_board,opponent_king,start_mood)
            if len(test)>0:
                return True
            else:
                new_board[opponent_king_index[0][0]][opponent_king_index[1][0]] = opponent_king
                new_board[mover[0]][mover[1]] = checked_king 
                new_board[kindx[0]][kindx[1]] = "0"

                checked_king_index = np.where(new_board == checked_king)
                kindx = (checked_king_index[0][0],checked_king_index[1][0])
                free_loc = ((kindx[0]-1,kindx[1]-1),(kindx[0]-1,kindx[1]+1),(kindx[0]+1,kindx[1]-1),(kindx[0]+1,kindx[1]+1))
                mover = free_loc[mover_indx]
                next_loc = new_board[mover[0]][mover[1]]
        return False
    if t:
        for i,item in enumerate(distance):
            if item == checker:
                return False
            else:
                board[kindx[0]][mover+i+1] = opponent_king
                board[opponent_king_index[0][0]][opponent_king_index[1][0]] = "0"
                test =  check_checker(board,opponent_king,start_mood)
                if len(test)>0:
                    return True
                else:
                    board[kindx[0]][mover+i+1] = "0"
                    board[opponent_king_index[0][0]][opponent_king_index[1][0]] = opponent_king                       
    else:
        return False
       
def run_king(board, checkers_list, all_symbols,start_mood):
    checked_king = checkers_list[-1]
    new_board = np.pad(board,1)
    checked_king_index = np.where(new_board == checked_king)
    row, col = (checked_king_index[0][0],checked_king_index[1][0])    
    king_next_move = [(row-1,col-1),(row-1,col),(row-1,col+1),(row,col-1),(row,col+1),(row+1,col-1),(row+1,col),(row+1,col+1)]
    
    for item in king_next_move:
        item_value = new_board[item[0]][item[1]]
        if (item_value in all_symbols) or item_value == 0:
            pass
        else:
            new_board[item[0]][item[1]] = checked_king
            new_board[row][col] = "0"
            board = new_board[1:9 , 1:9]
            checkers_list = check_checker(board, checked_king,start_mood)
            if len(checkers_list) == 0 :
                return True
            else:
                new_board[item[0]][item[1]] = "0"
                new_board[row][col] = checked_king
    return False

def checkmate(board, checkers_list, all_symbols, knight_symbols, start_mood, opponent_king):
    if len(checkers_list)==3:
        mate = run_king(board, checkers_list, all_symbols, start_mood)
        if mate:
            print(" you not checkemate , you can move king")
            return True
        else:
            print("you cant move king , you checkemate CUZ you double checked ")
            return False
    else:
        mate = fight(board, checkers_list, all_symbols, start_mood, opponent_king)  
        if mate:
            print("you not checkemate , you can fight whit checker")
            return True
        print("you cant fight whit checker")

        mate = run_king(board, checkers_list, all_symbols, start_mood)
        if mate:
            print("you not checkemate , you can move king")
            return True 
        print("you cant move king ")

        if checkers_list[0] in knight_symbols:
            print("you cant move king and fight  ,you are checkemate CUZ checker is  knight")
            return False
        
        mate = defense(board, checkers_list, all_symbols, start_mood, opponent_king)
        if mate:
            print("you not checkemate , you can defense ")
            return True
        print("you are checkemate , you cant fight or run king  or defens ")


kingsymbol = ["K","k"]
start_mood = (1,0)  # frist item is black start mood and secend itrm is white start mood (0 is down 1 is top)

for symbol in kingsymbol:
    checkers_list = check_checker(board, symbol,start_mood)
    if len(checkers_list) > 0:
        checkers_list.append(symbol)
        break
    
print("checkers_list:", checkers_list)
print("==================== check part end ========================")

if len(checkers_list)>0:
    print("we have check by",checkers_list[0],"on",checkers_list[-1])
    if checkers_list[-1] == kingsymbol[0]:
        knight_symbols = white_symbols[0:10]
        wking_symbol = kingsymbol[1]
        checkmate(board, checkers_list, black_symbols, knight_symbols, start_mood,wking_symbol)
    else:
        knight_symbols = black_symbols[0:10]
        bking_symbol = kingsymbol[0] 
        checkmate(board, checkers_list, white_symbols, knight_symbols, start_mood, bking_symbol)   
else:
    print("we dont have any check")


