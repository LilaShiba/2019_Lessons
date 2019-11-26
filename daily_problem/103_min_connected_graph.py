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
        
    

print(min_cont(graph, "a"))