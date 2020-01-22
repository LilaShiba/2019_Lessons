# This problem was asked by Amazon.
# 
# A binary tree is a mirror image of itself if its left and right subtrees 
# are identical mirror images i.e., the binary tree is symmetrical. 
# This is best explained with a few examples.
# 
#         4
#       / | \
#     3   5   3
#   /           \
# 9              9
# Given a k-ary tree, determine whether it is symmetric.


# elements at every lvl are palindromic

class Node:
    def __init__(self, value):
        self.v = value
        self.r = None
        self.l = None
    
def s_tree(node):
    # base case
    if not node:
        return True
    queue = get_lvl(node)
    for lvl in queue:
        if is_pal(lvl) == False:
            return False
    return True
    
def is_pal(q1):
    if q1 == q1[::-1]:
        return True
    return False

def get_lvl(node):
    queue = [node] # to drive code
    ans = [[node.v]] # for the answer hold values only
    while queue:
        next_lvl = []
        next_lvl_data = []
        for vertex in queue:
            if vertex.r:
                next_lvl.append(vertex.r)
                next_lvl_data.append(vertex.r.v)
            # to ensure mirror image, fill blank children with value as to account for such.
            else:
                next_lvl_data.append('#')
            if vertex.l:
                next_lvl.append(vertex.l)
                next_lvl_data.append(vertex.l.v)
            else:
                next_lvl_data.append('#')
        queue = next_lvl
        ans.append(next_lvl_data)
    return ans

def r_stree(left, right):
    # base case
    if not left and not right:
        return True
    # if uneven
    elif not left or not right:
        return False
    # check values
    elif left.v == right.v:
        return True 
    # ensure "mirror" image
    return r_stree(left.l, right.r ) and (r_stree(left.r, right.l))

def rr_stree(left,right):
    if not left and not right:
        return True
    elif not left or not right:
        return False
    elif left.l == right.r:
        return True
    return rr_stree(left.r, right.l) and rr_stree(left.l, right.r)
            
root = Node(1)
root.l = Node(2)
root.r = Node(2)
# root.r.r = Node(3)
# root.l.r = Node(3)
root.r.r = Node(3)
root.l.r = Node(4)
root.r.l = Node(4)
root.l.l = Node(3)
print(s_tree(root))
print(r_stree(root, root))
print(rr_stree(root,root))