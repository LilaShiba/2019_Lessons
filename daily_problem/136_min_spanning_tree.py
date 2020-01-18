# This problem was asked by Microsoft.
# 
# Recall that the minimum spanning tree is the subset of edges 
# of a tree that connect all its vertices with the smallest 
# possible total edge weight. Given an undirected graph with 
# weighted edges, compute the maximum weight spanning tree.
import pprint

class Graph:
    def __init__(self, n, m):
        self.graph = [[0 for x in range(n)]for y in range(m)]
    def showGraph(self):
        pprint.pprint(self.graph)
    def add_edge(self, loc, edge):
        self.graph[loc[0]][loc[1]] = edge
        

# graph = Graph(4,5)
# graph.add_edge((0,0), (0,1,2))
# graph.showGraph()

def find_min(tree, adj_list):
    best = float('inf')
    current = None
    for vertext in tree:
        for edge in adj_list[vertext]:
            if edge[0] not in tree and edge[1] < best:
                best = edge[1]
                current = edge[0]
                parent = vertext
    return current, parent
        

def prims(adj_list,start):
    tree = [start]
    connections = []
    
    while len(tree) < len(adj_list):
        next_vertex,parent = find_min(tree, adj_list)
        tree.append(next_vertex)
        connections.append((next_vertex, parent))
    return connections
            



adj_list = {
'a':[('b', 8), ('c', 6), ('d', 5)],
'b':[('a', 8), ('d', 4)],
'c':[('a',6), ('d', 3)],
'd':[('a',5), ('b',4), ('c',3)]
}

adj_list2 = {
'a':[('b',8), ('f',1), ('h', 6), ('e',5)],
'b':[('a',8), ('c',4), ('f',2)],
'c':[('b',4), ('f',2), ('g',7)],
'g':[('c',7), ('f',9)],
'f':[('g',9), ('c',2), ('b', 6), ('a',1), ('h',5)],
'h':[('f',5), ('a',6), ('e',3)],
'e':[('a',5), ('h',3)]
}

print(prims(adj_list2,'a'))
