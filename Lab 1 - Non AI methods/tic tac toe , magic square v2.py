
tic_tac_toe = [ ["-" , "o" , "x"] , ["o" , "-" , "-"] , ["-", "o" , "-"] ]

tic_tac_toe_position = [ ["0" , "1" , "2"] , ["3" , "4" , "5"] , ["6", "7" , "8"] ]
tic_tac_toe_base = [ ["-" for i in range(3)] for i in range(3)]



#print_board(magic_square)
def print_board(board):
    for row in board:
        for i in row:
            print(str(i),end = "\t")
        print("")
    print("")




def find2Same (tic_board : list):
    list_diagonal1 = [0,4,8]
    list_diagonal2 = [2,4,6]
    list_row1 = [0,1,2]
    list_row2 = [3,4,5]
    list_row3 = [6,7,8]
    list_col1 = [0,3,6]
    list_col2 = [1,4,7]
    list_col3 = [2,5,8]

    list_all = [list_diagonal1,list_diagonal2,list_row1,list_row2,list_row3,list_col1,list_col2,list_col3]

    # 2 same consecutive or 3 alternative
    for i in list_all:
        if (tic_board[i[0]//3][i[0]%3] == tic_board[i[1]//3][i[1]%3] and tic_board[i[1]//3][i[1]%3] != '-'):
            yield [i[0],i[1]]
        elif (tic_board[i[1]//3][i[1]%3]== tic_board[i[2]//3][i[2]%3] and tic_board[i[2]//3][i[2]%3] != '-'):
            yield [i[1],i[2]]
        elif(tic_board[i[0]//3][i[0]%3] == tic_board[i[2]//3][i[2]%3] and tic_board[i[2]//3][i[2]%3] != '-'):
            yield [i[0],i[2]]
    else:
        yield False            


def check_if_draw (tic_board : list):
    magic_square = [ [8 , 1 , 6] , [3 , 5 , 7] , [4 , 9 , 2] ]

    for same2list in find2Same(tic_board):
        if same2list != False:
            if ((y := magic_square[same2list[0]//3][same2list[0]%3] + magic_square[same2list[1]//3][same2list[1]%3]) < 1 or y > 9):
                return True
    return False

print_board(tic_tac_toe_base)
print(next(find2Same(tic_tac_toe)))



