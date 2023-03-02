

def print_board(state):
    for i in range(0, 9):
        print(state[i] , " " , end = "")
        if(i % 3 == 2):
            print('\n')

#solving 8 puzzle using hill climbing
class Node_8_puzzle_hill_climbing:
    
    def __init__(self , state , parent = None):
        self.state = state
        self.parent = parent
        self.children = []
        self.goal_state = [1, 2, 3, 8, " " , 4, 7, 6, 5]
        self.score = self.calculate_score()

    def print_board(self):
        for i in range(0, 9):
            print(self.state[i] , " " , end = "")
            if(i % 3 == 2):
                print('\n')
                
    def calculate_score(self):
        score = 0
        for i in range(0, 9):
            if(self.state[i] == self.goal_state[i]):
                score += 1
        return score

    def up(self):
        if(self.state.index(" ") > 2):
            temp = self.state.index(" ")
            child = self.state.copy()
            child[temp] , child[temp - 3] = self.state[temp - 3] , self.state[temp]
            return Node_8_puzzle_hill_climbing(child , self)
        else:
            return None
    def down(self):
        if(self.state.index(" ") < 6):
            temp = self.state.index(" ")
            child = self.state.copy()
            child[temp] , child[temp + 3] = self.state[temp + 3] , self.state[temp]
            return Node_8_puzzle_hill_climbing(child , self)
        else:
            return None
    def left(self):
        if(self.state.index(" ") % 3 != 0):
            temp = self.state.index(" ")
            child = self.state.copy()
            child[temp] , child[temp - 1] = self.state[temp - 1] , self.state[temp]
            return Node_8_puzzle_hill_climbing(child , self)
        else:
            return None
    def right(self):
        if(self.state.index(" ") % 3 != 2):
            temp = self.state.index(" ")
            child = self.state.copy()
            child[temp] , child[temp + 1] = self.state[temp + 1] , self.state[temp]
            return Node_8_puzzle_hill_climbing(child , self)
        else:
            return None
        
    def children_produce(self):
        children = []
        children.append(self.up())
        children.append(self.down())
        children.append(self.left())
        children.append(self.right())
        children = [x for x in children if x is not None]
        max_score = max(children , key = lambda x : x.score).score
        self.children = [x for x in children if x.score == max_score and max_score >= self.score]
        return self.children


def hill_climbing(start_state): 
    root = Node_8_puzzle_hill_climbing(start_state)   
    current = root
    stack = [root]
    while(len(stack) > 0):
        current = stack.pop()
        current.print_board()
        print("score = " , current.score , "\n------------------\n")
        
        if(current.score == 9):
            return current
        else:
            current.children = current.children_produce()
            stack += current.children


# result = Node_8_puzzle_hill_climbing(start_state).print_board()
# print(Node_8_puzzle_hill_climbing(start_state).score)
start_state = [" ", 3, 4, 1, 2, 5, 8, 7, 6]

result = hill_climbing(start_state)

