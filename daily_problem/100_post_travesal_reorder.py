# Asked by Google
#
# Given a sequence of keys visited by a postorder traversal of a bst,
# Recreate the tree.

# [

#         3
#     2     4   
#   1      5    6                     
    

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, data):
        if self.value:
            if data < self.value:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.value:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else: 
            self.value = data
        
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()
        

def postorder(node,arr,seq):
    if node:
        postorder(node.left, arr, seq)
        postorder(node.right, arr, seq)
        arr.append(node.value)
        seq.append(node)

    return arr, seq

def order(seq,arr):
    node = seq.pop(-1)
    next = [node]
    while next:
        node = next.pop(0)
        arr.append(node.value)
        if node.left:
            next.append(node.left)
        if node.right:
            next.append(node.right)            
    return arr

def make_tree(seq):
    root = seq.pop(0)
    root = Node(root)
    while seq:
        node = seq.pop(0)
        root.insert(node)
    return root
    
# test tree
root = Node(5)
for x in range(10):
    root.insert(x)



lst, sequence = postorder(root, [], [])
print(lst)
back_in_order = order(sequence, [])
print(back_in_order)
tree = make_tree(back_in_order)
tree.print_tree()
