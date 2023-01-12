

magic_square = [ [8 , 1 , 6] , [3 , 5 , 7] , [4 , 9 , 2] ]

tic_tac_toe = [ ["-" , "o" , "x"] , ["o" , "x" , "-"] , ["x", "o" , "-"] ]

def print_board(board):
    for row in board:
        for i in row:
            print(str(i),end = "\t")
        print("")
    print("")

#print_board(magic_square)
print_board(tic_tac_toe)

player_won = ""

#check if sum of any 3 postion is 15
for i in range (9):
    for j in range(9):
        for k in range(9):
            if(i!=j and i!=k and j!=k and tic_tac_toe[i//3][i%3] == tic_tac_toe[j//3][j%3] and \
                tic_tac_toe[i//3][i%3] == tic_tac_toe[k//3][k%3]):
                if(magic_square[i//3][i%3] + magic_square[j//3][j%3] + magic_square[k//3][k%3] == 15 ):
                    player_won = tic_tac_toe[i//3][i%3]
                
print(player_won + " won the game")

