import random

class Node:
    def __init__(self, v):
        self.v = v
        self.r = None
        self.l = None
        self.visited = False


def make_random_tree():
    root = Node(random.randint(0,10))
    
    if random.random() > 0.5:
        root.l = make_random_tree()
    if random.random() > 0.5:
        root.r = make_random_tree()
    return root

# gets deepest lvl
def get_lvl(root):
    if root is None:
        return 0
    
    r = get_lvl(root.r)
    l = get_lvl(root.l)
    
    return max(r,l) + 1

def inorder(root, target, lvl):
    if root == None:
        return 0
 
        
    if root.v == target:
        return lvl    
    r =  inorder(root.r, target, lvl+1)
    if r != 0:
        return r
    r = inorder(root.l, target, lvl+1)
    return r

def printLevel(root):
    height = get_lvl(root)
    for node in range(1, height+1):
        print_by_level(root,node)
        
def print_by_level(root, level):
        if root is None:
            return
        if level == 1:
            print(root.v)
        elif level > 1:
            print_by_level(root.l, level-1)
            print_by_level(root.r, level-1)

def get_target_by_lvl(root, lvl, target):
    if root == None:
        return 0
    
    if root.v == target:
        return lvl
    dl = get_target_by_lvl(root.l, lvl+1, target)
    if dl !=0:
        return dl
    dl = get_target_by_lvl(root.r, lvl+1, target)
    return dl
    
def bfs(root, target):
    queue = [root]
    lvl = 1
    while queue:
        node = queue.pop(0)
        if node == '#':
            lvl += 1
            continue
        
        if node.v == target:
            return True, lvl
            
        if node.visited == False:
            node.visited = True
            if node.r:
                queue.append(node.r)
            if node.l:
                queue.append(node.l)
            if node.l or node.r:
                queue.append('#')
    return False, lvl

def bfs(root, target):
    queue = [ (root,0) ]
    depth = 0
    
    while queue:
        node, d = queue.pop(0)
        if node.v == target:
            return depth
        
        if d > depth:
            depth += 1
        
        edges = [node.r, node.l]
        for edge in edges:
            if edge and edge.visited == False:
                queue.append((edge, depth+1))
                edge.visited = True


                
    return False, depth
                   
tree = make_random_tree()
# tree = Node(10)
# tree.l = Node(3)
# tree.r = Node(5)
# tree.r.r = Node(2)
# tree.r.l = Node(4)
# tree.l.l = Node(13)
# tree.l.r = Node(8)
#print('Tree height is ', get_lvl(tree))
#print('Node is at ', inorder(tree,4,0))
print('Node is at', get_target_by_lvl(tree,0, 4))
print('Node is at ', bfs(tree, 4))
    