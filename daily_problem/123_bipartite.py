# This problem was asked by Dropbox.
# 
# Given an undirected graph G, check whether it is bipartite. 
# Recall that a graph is bipartite if its vertices can be divided 
# into two independent sets, U and V, such that no edge connects 
# vertices of the same set.
import random, pprint
class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = [[random.randint(0,1) for column in range(v)]for row in range(v)]
    
    def showGraph(self):
        pprint.pprint(self.graph)
        
    def is_bipartite(self,src):
        # create color array to store colors of v
        color_arr = [-1] * self.v
        # set first node color
        color_arr[src] = 1
        # create a queue for bfs
        queue = []
        queue.append(src)
        # bfs
        while queue:
            u = queue.pop()
            # check edges
            for v in range(self.v):
                if self.graph[u][v] == 1 and color_arr[v] == -1:
                    color_arr[v] = 1 - color_arr[u]
                    queue.append(v)
                elif self.graph[u][v] == 1 and color_arr[u] == color_arr[v]:
                    return False
        return True
        
                    
        

adj_list = {
0: [3],
1: [2,3],
2: [3,5],
3: [4,5],
4: [2],
5: [1,4]
}

def bipartite(adj_list, colors=[]):
    if len(colors) == len(adj_list):
        return True, colors
    
    # try each option aka backtrack if needed
    for i in range(2):
        colors.append(i)
        # does it meet parameters of problem
        if is_safe(adj_list, colors):
            # recursive iteration: drives code
            if bipartite(adj_list, colors):
                return True, colors 
        colors.pop()
    return False

def is_safe(adj_list, colors):
        last_color = colors[-1]
        last_vertex = len(colors)-1
        neighbors = [x for x in adj_list[last_vertex] if x < last_vertex]

        for neighbor in neighbors:
            if colors[neighbor] == last_color:
                return False
        return True
    
    
        
print(bipartite(adj_list))    
# g = Graph(3)
# g.showGraph()
# print(g.is_bipartite(0))
