class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        myNode = Node(val)
        
        if self.root is None:
            self.root = myNode
            return 
    
        current = self.root
        while current:
            if current.info > val:
                if current.left is  None:
                    current.left = myNode
                    return
                current = current.left
                
            else :
                if current.right is  None:
                    current.right = myNode
                    return
                current = current.right
                

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
