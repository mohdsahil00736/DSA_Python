class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, value):
    if(root == None):
        return Node(value)
    if(root.data == value):
        return root 
    if(root.data < value):
        root.right = insert(root.right, value)
    else:
        root.left = insert(root.left, value)
    return root

def search(root, value):
    if(root == None):
        print("Element Not found  \n ")
        return 
    if(root.data == value):
        print("\nElement found ")
        return  
    elif(root.data < value):
       search(root.right, value)
    else:
        search(root.left, value)
    
def Inorder(root):
    if (root != None):
        Inorder(root.left)
        print(root.data , end = " ")
        Inorder(root.right)       


# make a tree by normal likedlist   

# root = Node(20)
# root.left = Node(15)
# root.left.left = Node(12)
# root.left.right = Node(18)
# root.right = Node(30)
# root.right.right = Node(40)


root = insert(None,20)
root = insert(root, 15)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 25)
root = insert(root, 45)
root = insert(root, 10)

Inorder(root)

search(root,40)
search(root, 100)