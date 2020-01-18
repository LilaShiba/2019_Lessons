# def make_trie(words):
#     trie = {}
#     for word in words:
#         current = trie
#         for letter in word:
#             current = current.setdefault(letter,{})
#         trie['#'] = '#'
#     return trie
# 
# 
# words = ['taco', 'cat', 'tacocat']
# print(make_trie(words))
# 
# def dfs(node, adj_list, visited, order):
#     if node not in visited:
#         visited.append(node)
#         order.append(node)
#         for edge in adj_list[node]:
#             if edge not in visited:
#                 dfs(edge, adj_list, visited, order)
#     return visited
# 
# def search_(adj_list, node, visited, order):
#     if node not in visited:
#         visited.append(node)
#         order.insert(0, node)
#         for edge in adj_list[node]:
#             search_(adj_list, edge, visited, order)
#     return order
# def topo(adj_list):
#     visited = []
#     order = []
#     for vertex in adj_list:
#         dfs(vertex,adj_list,visited, order)
#     return order
# 
# def ts(adj_list):
#     visited = order = []
#     for node in adj_list:
#         search_(adj_list, node, visited, order)
# def make_trie(words):
#     trie = {}
#     for word in words:
#         current_trie = trie
#         for letter in word:
#             current_trie = current_trie.setdefault(letter, {})
#         trie["#"] = '#'
#     return trie
# 
# graph = {
#     1:[2,3],
#     2:[3,1,4],
#     3:[4,2],
#     4:[]
# }
# words = ['meow', 'meoow', 'woof', 'woofer']
# print(topo(graph))
# print(ts(graph))
# print(make_trie(words))

def fib(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

def fib1(n):
    if n <= 1:
        return n 
    else:
        for _ in range(n):
            a,b = b, a+b 
        return a
        
print(fib(15))
print(fib(15))