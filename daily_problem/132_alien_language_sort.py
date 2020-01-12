# This problem was asked by Airbnb.
# 
# You come across a dictionary of sorted words in a 
# language you've never seen before. Write a program 
# that returns the correct order of letters in this language.
# 
# For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], 
# you should return ['x', 'z', 'w', 'y'].


# source https://www.dailycodingproblem.com/solution/226?token=f8c9c5ddad19bfbd4a508a8eec0df478aab7ac3cce072925c1aa44d34ac639c69ccf85b5

from collections import deque
arr = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']
ans = ['x', 'z', 'w', 'y']

def create_graph(words):
    # get each unique letter
    letters = set(''.join(words))
    # make dictionary where each letter has blank [] as value
    graph = {letter: [] for letter in letters}
    # make pairwise comparisons 
    for pair in zip(words, words[1:]):
        # * is for unzipping values 
        for before, after in zip(*pair):
            # add before if after is a different value
            if before != after:
                graph[before].append(after)
                break
    return graph


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for edge in graph[node]:
            dfs(graph,edge,visited)
    return visited

# dfs that keeps order
def visit_dfs(letter, graph, visited, order):
    visited.add(letter)
    for edge in graph[letter]:
        if edge not in visited:
            visit_dfs(edge,graph,visited,order)
    order.appendleft(letter)
    
def topo_sort(graph):
    visited = set()
    order = deque([])
    
    for letter in graph:
        if letter not in visited:
            visit_dfs(letter,graph,visited,order)
    return list(order)
     

def alien_sort(arr):
    graph = create_graph(arr)
    ans = topo_sort(graph)
    return ans    
        
    
print(alien_sort(arr))