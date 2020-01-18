def dfs(adj_list, visited, node, order, target=None):
    if node not in visited:
        visited.append(node)
        order.insert(0,node)
        for edge in adj_list[node]:
            dfs(adj_list, visited, edge, order)
    return order
    

def topo_sort(adj_list):
    visited = []
    order = []
    for vertex in adj_list:
        if vertex not in visited:
            dfs(adj_list, visited, vertex, order)
    return visited


def dfs_helper(adj_list, visited, node, order):
    if node not in visited:
        visited.append(node)
        order.insert(0, node)
        for edge in adj_list[node]:
            dfs_helper(adj_list, visited, edge, order)
    return order
    
def topo(adj_list):
    visited = []
    order = []
    
    for node in adj_list:
        dfs_helper(adj_list, visited, node, order)
    return visited
    
    
def search(adj_list, visited, node, order):
    if node not in visited:
        visited.append(node)
        order.append(node)
        for edge in adj_list[node]:
            search(adj_list, visited, edge, order)
        return order

def t(adj_list):
    visited = []
    order = []
    for vertex in adj_list:
        search(adj_list, visited, vertex, order)
    return order
    
    
adj_list = {
    1:[2],
    2:[3],
    3:[],
    4:[]
}


def tp(adj_list):
    order = []
    visited = []
    
    for node in adj_list:
        if node not in visited:
            dfs_h(adj_list, visited, order, node)
    return order
    
def dfs_h(adj_list, visited, order, node):
    visited.append(node)
    order.append(node)
    for edge in adj_list[node]:
        if edge not in visited:
            dfs_h(adj_list,visited,order,edge)
    

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

print(topo_sort(graph))
print(topo(graph))
print(tp(graph))
print(t(graph))