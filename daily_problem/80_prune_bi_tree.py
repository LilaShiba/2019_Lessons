# given a binary tree of all 1 and 0's 
# prune all subtrees comprised of 0's

class Node():
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.subtree = False

def prune_me(node,arr):
    if node:
        prune_me(node.left,arr)
        if node.left != None or node.right != None:
            arr.append(node.data)
        elif node.data == 0:
            print('pruned')
        else:
            arr.append(node.data)
        prune_me(node.right, arr)
    return arr
    
def get_depth(node):
    if not node:
        return 0
    l = get_depth(node.left)
    r = get_depth(node.right)
    return max(l,r) + 1

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(0)
    root.left.right = Node(1)
    root.left.left = Node(0)
    root.right = Node(1)
    root.right.right = Node(1)
    root.right.left = Node(0)
    print(get_depth(root))
    print(prune_me(root, []))
    