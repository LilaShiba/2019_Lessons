import collections
class Node():
    
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None
        # new traits
        self.sums = {}
        self.max_freq = 0
        self.max_vals = []
        
def get_mean(node,ans=[]):
    
    def dfs(node, ans):
        # base case hit the tree bottom
        if not node:
            return 0
        
        cur_sum = (node.val + dfs(node.right,ans) + dfs(node.left,ans))
        ans.append(cur_sum)
        return cur_sum
    
    current = node.val
    cache = {}
    
    for x in ans:
        if x not in cache:
            cache[x] = 1
        else:
            cache[x] += 1
    return max(cache)
    
def get_most(root):
    if not root:
        return []
    
    cache = collections.defaultdict(int)
    def cal_sum(node):
        if not node:
            return 0
        s = node.val + cal_sum(node.right) + cal_sum(node.left)
        cache[s] += 1
        return s
    cal_sum(root)
    mx = max(cache.values())
    return [k for k, v in cache.items() if v == mx]
    
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    
    root.right.right = Node(3)
    root.right.left = Node(7)
    
    root.left.left = Node(5)
    root.left.right = Node(5)
    print(get_mean(root))
    print(get_most(root))
    #level = height(root)
    #deepest_node(root,level)
    #inorder(root)
    #post_order(root)
    