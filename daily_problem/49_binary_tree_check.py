class Node():
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.root = False

def binary_tree_check(root, l=None, r=None):
    if root is None:
        return True
    if (l != None and root.data <= l.data):
        return False
    if (r != None and root.data >= r.data):
        return False
    return binary_tree_check(root.left, l, root) and binary_tree_check(root.right, root, r)

def isValidBST(root) :
    stack, inorder = [], float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= inorder:
            return False
            
        inorder = root.val
        root = root.right
    return True    
        
    
root = Node(10)
root.left = Node(6)
root.right = Node(12)
root.right.right = Node(100)
root.right.left = Node(11)
root.left.left = Node(1)
root.left.right = Node(7)
print(binary_tree_check(root))

        #             10
        #         6       12
        # 1   5               50  100 
        
        

    