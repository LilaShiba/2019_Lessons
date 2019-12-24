# This problem was asked by Dropbox.
# 
# Given an undirected graph G, check whether it is bipartite. 
# Recall that a graph is bipartite if its vertices can be divided 
# into two independent sets, U and V, such that no edge connects 
# vertices of the same set.
import random, pprint
class Graph:
    def __init__(self, v):
        self.v = len(v)
        self.graph = v
        
    def make_matrix(self, v):
        n = range(len(v))
        maze = [[0 for x in n]for y in n]
        
        for x,y in v.items():
            for items in y:
                maze[x][items] = 1 
                maze[items][x] = 1
        self.graph = maze
        return maze
    
    def showGraph(self):
        pprint.pprint(self.graph)
        
    def is_safe(self, color_history, potential_color, current_node):
        #print(self.graph[current_node])
        for edge in range(self.v):
            #print('edge:', edge)
            if self.graph[current_node][edge] == 1: 
                #print('hi',self.graph[current_node][edge])
                if potential_color == color_history[edge]:
                    return False
        return True
    
    def backtrack_helper(self, color_history, perms, node):
        if node == self.v:
            return True
        
        for perm in range(0,perms):
            if self.is_safe(color_history, perm, node) == True:
                color_history[node] = perm
                if self.backtrack_helper(color_history, perms, node+1) == True:
                    return True
                color_history[node] = 0
        return False
                
    def backtrack(self, perms):
        color_history = [-1] * self.v
        node = 0
        if self.backtrack_helper(color_history, perms, node) == False:
            return False
        return color_history
    
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
2: [1,3,5],
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
        # check nodes that have been used
        neighbors = [x for x in adj_list[last_vertex] if x < last_vertex]

        for neighbor in neighbors:
            if colors[neighbor] == last_color:
                return False
        return True
    
def helper(graph, start, colors):
    queue = [start]
    colors[start] = 1

    while queue:
        vertex = queue.pop(0)

        for neighbor in graph[vertex]:
            if colors[neighbor] == 0:
                colors[neighbor] = -colors[vertex]
                queue.append(neighbor)
            elif colors[neighbor] == colors[vertex]:
                return False

    return True

def is_bipartite(graph):
    colors = [0 for _ in range(len(graph))]
    for vertex in graph.keys():
        if colors[vertex] == 0:
            if not helper(graph, vertex, colors):
                return False

    return True    
        
#print(bipartite(adj_list))  
#print(is_bipartite(adj_list))  
g = Graph(adj_list)
g.make_matrix(adj_list)
g.showGraph()
print(g.backtrack(5))
#print(g.back_driver(2))
#print(g.is_bipartite(adj_list))
