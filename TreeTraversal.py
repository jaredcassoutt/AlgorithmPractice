class Tree():
    def __init__(self,root):
        self.root = root
        
    def DFS(self):
        '''
        Depth-first search method for tree traversal which 
        utilizes a stack to traverse from the top down and
        prints each element's value.
        '''
        DFS_array = [self.root]
        while DFS_array != []:
            if DFS_array[0].children != []:
                parent = DFS_array.pop(0)
                print(parent.value)
                DFS_array = parent.children + DFS_array
            else:
                removal = DFS_array.pop(0)
                print(removal.value)
                
    def BFS(self):
        '''
        Breadth-first search method for tree traversal which 
        utilizes a queue to traverse row by row and prints
        each element's value.
        '''
        BFS_array = [self.root]
        while BFS_array != []:
            if BFS_array[0].children != []:
                parent = BFS_array.pop(0)
                print(parent.value)
                BFS_array = BFS_array + parent.children
            else:
                removal = BFS_array.pop(0)
                print(removal.value)

class TreeNode():
    def __init__(self,value):
        self.value = value
        self.children = []
