# Deletion have 3 Cases : 
# 1. Node to be deleted is a leaf node have zero child
# 2. Node to be deleted has only one child
# 3. Node to be deleted has two child

class Node :
    def __init__(self, value):
        self.right = None
        self.left = None
        self.data = value

def get_successor(root):
    root = root.right
    while(root != None and root.left != None):
        root = root.left
    return root
        
def delete(root, value):
    if(root.data == None):
        return root
    if (root.data > value):
        root.left = delete(root.left, value)
    elif(root.data < value):
        root.right = delete(root.right, value)
    else:
        if (root.left == None):                     # thid portion is for case 1 and case 2 -> have zero or one child
            return root.right
        if (root.right == None):
            return root.left
        else:                                       # this portion is for case 3 -> have two child
            succ = get_successor(root)
            root.data = succ.data
            root.right = delete(root.right, succ.data)
    return root


def Inorder(root):
    if (root!= None):
        Inorder(root.left)
        print(root.data, end = " ")
        Inorder(root.right)


root = Node(20)
root.left = Node(15)
root.left.left = Node(12)
root.left.right = Node(18)
root.right = Node(30)
root.right.left = Node(25)
root.right.right = Node(40)
root.right.right.right = Node(50)


Inorder(root)
print("\n")
delete(root, 12)   # case 1 -> have zero child
delete(root, 40)   # case 2 -> have one child
delete(root, 30)   # case 3 -> have two child
Inorder(root)

