# water Jug with 4 and 3 liters solved using BFS


class Node:
    def __init__(self ,left_max , right_max , Value : list = [0 , 0], parent = None, depth = 0 ):
        self.Value = Value
        self.parent = parent
        self.depth = depth
        self.children = []
        self.left_max = left_max
        self.right_max = right_max
        print(self.Value , self.depth)
        
    def left_fill(self):
        if(self.Value[0] != self.left_max):
            return Node(self.left_max , self.right_max ,[self.left_max , self.Value[1]] , self , self.depth + 1)
        else:
            return None
    def right_fill(self):
        if(self.Value[1] != self.right_max):
            return Node(self.left_max , self.right_max ,[self.Value[0] , self.right_max] , self , self.depth + 1)
        else:
            return None
    def left_empty(self):
        if(self.Value[0] != 0):
            return Node(self.left_max , self.right_max ,[0 , self.Value[1]] , self , self.depth + 1)
        else:
            return None
    def right_empty(self):
        if(self.Value[1] != 0):
            return Node(self.left_max , self.right_max ,[self.Value[0] , 0] , self , self.depth + 1)
        else:
            return None
    def left_to_right(self):
        if(self.Value[0] != 0 and self.Value[1] != self.right_max):
            if(self.Value[0] + self.Value[1] <= self.right_max):
                return Node(self.left_max , self.right_max ,[0 , self.Value[0] + self.Value[1]] , self , self.depth + 1)
            else:
                return Node(self.left_max , self.right_max ,[self.Value[0] - (self.right_max - self.Value[1]) , self.right_max] , self , self.depth + 1)
        else:
            return None
    def right_to_left(self):
        if(self.Value[1] != 0 and self.Value[0] != self.left_max):
            if(self.Value[0] + self.Value[1] <= self.left_max):
                return Node(self.left_max , self.right_max ,[self.Value[0] + self.Value[1] , 0] , self , self.depth + 1)
            else:
                return Node(self.left_max , self.right_max ,[self.left_max , self.Value[1] - (self.left_max - self.Value[0])] , self , self.depth + 1)
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
def BFS(accepted_states : list , left_max, right_max):
    start = Node(left_max , right_max ,[0 , 0] , None , 0)
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



right_max = 4
left_max = 3
accepted_states = [[2 , i] for i in range (right_max +1)]

result = BFS(accepted_states, left_max,right_max)

print("\nresult" ,result.Value , result.depth)
# printing solution path
print_path(result)


    





