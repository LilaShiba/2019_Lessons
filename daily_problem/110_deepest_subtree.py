class Node():
    
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    
def get_tree(node):    
    def get_lvl(node):
        if not node:
            return 0    
        l = get_lvl(node.left)
        r = get_lvl(node.right)
        return max(l,r)+1
    
    depth = {None:-1}
    def dfs(node,parent=None):
        if node:
            depth[node.val] = depth[parent] + 1
            dfs(node.left, node.val)
            dfs(node.right, node.val)
            
    
    dfs(root)
    print(depth)    


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.left.left = Node(5)
    root.right.right.right = Node(10)
    print(get_tree(root))
    #level = height(root)
    #deepest_node(root,level)
    #inorder(root)
    #post_order(root)
    