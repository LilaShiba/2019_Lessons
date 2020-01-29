arr = ['eon', 'tree', 'hat']
arr2 = ['chair', 'height', 'racket', 'touch', 'tunic']
arr3 = ['cat', 'tack', 'keep', 'peep']

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
    arr = sorted(arr, key=lambda x:x[0])
    adj_list = {}
    for x in arr:
        adj_list[x] = [word for word in arr if word[0] == x[-1] and word != x]
    print(adj_list)

    ans = topo_sort(adj_list)
    return ans
    
def  dfs(adj_list, node, cache):
  if node not in cache:
    cache.insert(0, node)
    for edge in adj_list[node]:
      dfs(adj_list, node, cache)
  return cache

def topo_sort(adj_list):
  cache = []
  for vertex in adj_list:
      dfs(adj_list, vertex, cache)
  return cache

def circle_list(arr):
  #arr = sorted(arr, key=lambda x:x[0])
  adj_list = {}
  for x in arr:
    adj_list[x] = [word for word in arr if word[0] == x[-1] and word != x]
  #print(adj_list)
  ans2 = circle_find(adj_list)
 # ans = topo_sort(adj_list)
  return ans2

def circle_find(adj_list):
    start = []
    ans = []
    
    for x in adj_list:
        if len(adj_list[x]) == 0:
            start.append(x)
    print(adj_list)

    if len(start) > 1:
        return False
    if len(start) == 0:
        start.append(x)
    
    word = start.pop()
    ans.append(word)
    
    while len(ans) < len(adj_list):
        for x in adj_list:
            if word in adj_list[x] and x not in ans:
                word = x
                ans.insert(0,word)
                print(ans)
    return ans
        


print(circle_list(arr2))