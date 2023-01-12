print("Enter a odd no to for that no sided magic square")
n = int(input("odd no - "))

#print(n)



class magic_square:
    
    def _next_position(self):
        y_n = (self.y-1) % n
        x_n = (self.x+1) % n
        if(self.magic_square[y_n][x_n] is None):
            self.x , self.y  = x_n , y_n
        else:
            self.y = (self.y+1) % n


    def __init__(self , n):

        self.magic_square = list()
        middle_value = n//2
        self.y = 0
        self.x = middle_value   
        for i in range(n):
            #magic_square.append([None]*n)
            self.magic_square.append([None for i in range(n)])

        for i in range(1 ,n**2+1):
            self.magic_square[self.y][self.x] = i
            self._next_position()

    def printm(self):
        for row in self.magic_square:
            for i in row:
                print(str(i),end = "\t")
            print("")




magic_square(n).printm()