
#will give solution of N queen problem using backtracking
class NQueenProblem:

    def __init__(self, n):
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.solutions = 0

    def isSafe(self, row, col):
        #check if there is a queen in the row
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        #check if there is a queen in the upper diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        #check if there is a queen in the lower diagonal
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve(self, col):
        if col >= self.n:
            self.solutions += 1
            print("Solution #", self.solutions)
            self.print_board()
            return

        for i in range(self.n):
            if self.isSafe(i, col):
                self.board[i][col] = 1
                self.solve(col + 1)
                self.board[i][col] = 0

    def Solution(self):
        self.solve(0)
        print("Total solutions:", self.solutions)
    
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end = " ")
            print()
        print("")


n = int(input("input n for N queen problem -"))

NQueenProblem(n).Solution()