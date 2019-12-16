import b_tree # data, left, right

def pre_order(root):
        # (root,left,right)
    nodeStack = [root]
    while nodeStack:
        node = nodeStack.pop()
        print(node.data)

        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)

def iterative_preorder(node):
    stack = []
    
    while node or stack:
        while node:
            stack.append(node)
            print(node.data)
            node = node.left
        node = stack.pop()
        node = node.right
        
        
root = b_tree.Node(10)
root.left = b_tree.Node(8)
root.right = b_tree.Node(9)
root.left.left = b_tree.Node(3)
root.left.right = b_tree.Node(5)
root.right.left = b_tree.Node(2)


print('pre_order')
#pre_order(root)
print(iterative_preorder(root))
