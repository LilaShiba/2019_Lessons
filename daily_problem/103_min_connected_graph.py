# This problem was asked by Facebook.
# 
# A graph is minimally-connected if it is connected and there 
# is no edge that can be removed while still leaving the graph connected. 
# For example, any binary tree is minimally-connected.
# 
# Given an undirected graph, check if the graph is minimally-connected. 
# You can choose to represent the graph as either an adjacency matrix or adjacency list.

# Bellman Ford detects negative cycles
# Use DFS to detect cycle
# Easy af because it is undirected

import random, pprint

adj_list = {
    1: [4],
    2: [3],
    3: [1],
    4: [2]
}

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
        
Wgraph = {

            's': {'a': 0, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}
            }

def min_connect(adj_list):
    seen = []
    for x in adj_list:
        for y in adj_list[x]:
            if y in seen:
                return False
            seen.append(y)
    return True
    
def min_cont(adj_list,start):
    stack = [start]
    explored = []
    
    while stack:
        node = stack.pop(0)
        explored.append(node)
        
        for x in adj_list[node]:
            if x not in explored:
                stack.append(x)
    return explored
        
def bellmanFord(adj_list, start):
    dist = {}
    # set distances to inif
    for node in adj_list:
        dist[node] = float('inf')
    dist[start] = 0
    unseenNodes = adj_list
    
    for x in range(len(unseenNodes)-1):
        for u in unseenNodes:
            # relax
            for v,w in unseenNodes[u].items():
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u]+ w 
    
    for u in unseenNodes:
        for v,w in unseenNodes[u].items():
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return 'Neg Cycle'
    
    return dist
         

#print(min_cont(graph, "a"))
print(bellmanFord(Wgraph,'s'))