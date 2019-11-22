# Asked by Google
#
# Given a sequence of keys visited by a postorder traversal of a bst,
# Recreate the tree.

# [4 5 2 3 1] would be 

#         1
#      2    3
#   4    5   

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder(node,arr,seq):
    if node:
        postorder(node.left, arr, seq)
        postorder(node.right, arr, seq)
        arr.append(node.value)
        seq.append(node)

    return arr, seq

def make_tree(seq,arr):
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

# test tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
lst, sequence = postorder(root, [], [])
print(lst)
tree = make_tree(sequence, [])
print(tree)