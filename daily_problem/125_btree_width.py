class Node:
    def __init__(self,v):
        self.v = v
        self.r = None
        self.l = None
        
        
def width(root):
    hash_table = htable(root, {})
    return max(hash_table), min(hash_table), hash_table
    
def htable(root, table, dist=0, lvl = 0):
    if not root:
        return []
        
    if dist not in table or table[dist][1] <= lvl:
        table[dist] = (root.v, lvl)
    
    htable(root.l, table, dist-1, lvl+1)
    htable(root.r,table,dist+1,lvl+1)
    return table

def width2(root):
    htable = make_table(root, {})
    print(htable)

def make_table(root, table, dist=0, lvl=0):
    if not root:
        return []
    if dist not in table:
        table[dist] = (root.v, lvl)
    
    make_table(root.l, table, dist-1, lvl+1)
    make_table(root.r, table, dist+1, lvl+1)
    
    return max(table), min(table), table

if __name__ == "__main__":
    root = Node(10)
    root.l = Node(5)
    root.r = Node(15)
    root.r.r = Node(4)
    root.l.l = Node(3)
    root.l.r = Node(2)
    root.r.l = Node(8)
    print(width(root))
    print(width2(root))