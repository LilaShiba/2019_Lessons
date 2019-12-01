class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
    

def height(node):
    if node is None:
        return 0
    l = height(node.left)
    r = height(node.right)
    return max(l,r)+1

def print_by_level(node, lvl):
    if node is None:
        return
    if lvl == 1:
        print(node.val)
    elif lvl > 1:
        print_by_level(node.right, lvl-1)
        print_by_level(node.left, lvl-1)
    
def print_height(node):
    lvl = height(node)
    for x in range(1, lvl+1):
        print_by_level(node,x)

def by_lvl(root):
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
        print(node.val)
        
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.left.left = Node(5)
    root.right.right.right = Node(10)
    print(print_height(root))
    print(by_lvl(root))