# water Jug with 4 and 3 liters solved using BFS




class Node:
    def __init__(self, Value : list = [0 , 0], parent = None, depth = 0 , left_max = 4 , right_max = 3):
        self.Value = Value
        self.parent = parent
        self.depth = depth
        self.children = []
        self.left_max = left_max
        self.right_max = right_max
        print(self.Value , self.depth)
        
    def left_fill(self):
        if(self.Value[0] != self.left_max):
            return Node([self.left_max , self.Value[1]] , self , self.depth + 1)
        else:
            return None
    def right_fill(self):
        if(self.Value[1] != self.right_max):
            return Node([self.Value[0] , self.right_max] , self , self.depth + 1)
        else:
            return None
    def left_empty(self):
        if(self.Value[0] != 0):
            return Node([0 , self.Value[1]] , self , self.depth + 1)
        else:
            return None
    def right_empty(self):
        if(self.Value[1] != 0):
            return Node([self.Value[0] , 0] , self , self.depth + 1)
        else:
            return None
    def left_to_right(self):
        if(self.Value[0] != 0 and self.Value[1] != self.right_max):
            if(self.Value[0] + self.Value[1] <= self.right_max):
                return Node([0 , self.Value[0] + self.Value[1]] , self , self.depth + 1)
            else:
                return Node([self.Value[0] - (self.right_max - self.Value[1]) , self.right_max] , self , self.depth + 1)
        else:
            return None
    def right_to_left(self):
        if(self.Value[1] != 0 and self.Value[0] != self.left_max):
            if(self.Value[0] + self.Value[1] <= self.left_max):
                return Node([self.Value[0] + self.Value[1] , 0] , self , self.depth + 1)
            else:
                return Node([self.left_max , self.Value[1] - (self.left_max - self.Value[0])] , self , self.depth + 1)
        else:
            return None
        
    def generate_children(self):
        self.children.append(self.left_fill())
        self.children.append(self.right_fill())
        self.children.append(self.left_empty())
        self.children.append(self.right_empty())
        self.children.append(self.left_to_right())
        self.children.append(self.right_to_left())
        self.children = [child for child in self.children if child is not None]
        return self.children


# implement BFS generation of tree
def BFS(start : Node, accepted_states : list):
    queue = [start]
    already_visited = []
    
    while(len(queue) != 0):
        current = queue.pop(0)
        
        if(current.Value in already_visited):
            continue
        else:
            already_visited.append(current.Value)
            
        if(current.Value in accepted_states):
            return current
        
        queue.extend(current.generate_children())
    return None
    
def print_path(result : Node):
    path = []
    
    while(result.parent is not None):
        path.append(result.Value)
        result = result.parent
    
    path.append(result.Value)
    path.reverse()
    print(path)



accepted_states = [[2 , 0] , [2, 1] , [2, 2] , [2, 3]]
right_max = 3
left_max = 4

result = BFS(Node([0 , 0] , None , 0 , left_max , right_max) , accepted_states)

print("\nresult" ,result.Value , result.depth)


# printing solution path
print_path(result)


    





