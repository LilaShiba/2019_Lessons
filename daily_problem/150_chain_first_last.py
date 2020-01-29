arr = ['eon', 'tree', 'hat']
arr2 = ['chair', 'height', 'racket', 'touch', 'tunic']
arr3 = ['cat', 'keep', 'tack', 'peep']

# def chain_circle(arr):
#     # O(logN)
#     sarr = sorted(arr, key = lambda x: x[-1] )
#     ans = [sarr[0]]
#     for idx in range(1, len(sarr)):
#         if arr[idx][0] == arr[idx-1][-1]:
#             ans.insert(idx, arr[word])
# 
# 
#     return ans

def chain_circle(arr):
    adj_list = {}
    for x in arr:
        adj_list[x] = [word for word in arr if word[-1] == x[0] and word != x]
    print(adj_list)

    ans = topo_sort(adj_list)
    return ans
    
def dfs(adj_list, node, cache):
    if node not in cache:
        cache.insert(0, node)
        for x in adj_list[node]:
            dfs(adj_list, x, cache)
    return 
        
def topo_sort(adj_list):
    cache = []
    for node in adj_list:
        dfs(adj_list, node, cache)
    return cache
                
print(chain_circle(arr3))