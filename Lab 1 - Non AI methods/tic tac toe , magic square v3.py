
#tic_tac_toe = [ ["-" , "o" , "x"] , ["o" , "-" , "-"] , ["-", "o" , "-"] ]

tic_tac_toe_position = [ ["0" , "1" , "2"] , ["3" , "4" , "5"] , ["6", "7" , "8"] ]
tic_tac_toe_base = [ ["-" for i in range(3)] for i in range(3)]
magic_square = [ [8 , 1 , 6] , [3 , 5 , 7] , [4 , 9 , 2] ]
remaining_position = [i for i in range(0 ,9)]


#print_board(magic_square)
def print_board(board):
    for row in board:
        for i in row:
            print(str(i),end = "\t")
        print("")
    print("")

def convert_to_magic_no(position):
    position = int(position)
    return magic_square[position//3][position%3]

def player_won(player_positions , remaining_position):

    for i in player_positions:
        for j in player_positions:
            for k in player_positions:
                if(i!=j and i!=k and j!=k):
                    if(convert_to_magic_no(i) + convert_to_magic_no(j) + convert_to_magic_no(k) == 15 ):
                        return 1
    for i in remaining_position:
        for j in remaining_position:
            for k in remaining_position:
                if(i!=j and i!=k and j!=k):
                    if(convert_to_magic_no(i) + convert_to_magic_no(j) + convert_to_magic_no(k) == 15 ):
                        return 0
    for i in remaining_position:
        for j in remaining_position:
            for k in player_positions:
                if(i!=j and i!=k and j!=k):
                    if(convert_to_magic_no(i) + convert_to_magic_no(j) + convert_to_magic_no(k) == 15 ):
                        return 0   
    for i in remaining_position:
        for j in player_positions:
            for k in player_positions:
                if(i!=j and i!=k and j!=k):
                    if(convert_to_magic_no(i) + convert_to_magic_no(j) + convert_to_magic_no(k) == 15 ):
                        return 0
                    else:
                        return -1


a = 'x'
b = 'o'
a_position = []
b_position = []
for i in range(9):
    print_board(tic_tac_toe_base)
    print("position are follows")
    print_board(tic_tac_toe_position)
    if(i%2 == 0):
        print("Player 1 turn")
        position = int(input("Enter position: "))
        if(position in remaining_position):
            remaining_position.remove(position)
            tic_tac_toe_base[position//3][position%3] = a
            a_position.append(int(position))
        else:
            print("Position already taken")
            i -= 1
    else:
        print("Player 2 turn")
        position = int(input("Enter position: "))
        if(position in remaining_position):
            remaining_position.remove(position)
            tic_tac_toe_base[position//3][position%3] = b
            b_position.append(int(position))
        else:
            print("Position already taken")
            i -= 1
    print_board(tic_tac_toe_base)
    if((a_out := player_won(a_position, remaining_position)) == 1):
        print("Player " + a + " won")
        break;
    elif((b_out := player_won(b_position, remaining_position)) == 1):
        print("Player " + b + " won")
        break;
    elif(a_out == -1 or b_out == -1):
        print("Draw")
        print_board(tic_tac_toe_base)

        break;
    else:
        print("Continue")

