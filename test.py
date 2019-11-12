import random
import pprint
matrix = [[random.randint(0,1) for x in range(5)] for y in range(5)]
pprint.pprint(matrix)
# preprocess into largest connected groups
def find_biggest_area(matrix):
    length = len(matrix)
    cache = []
    areas = {}

    for x in range(length):
        for y in range(length):
            if (x,y) not in cache:
                cache,areas = bfs(cache,matrix,(x,y),areas)
    return areas
def safe(cx,cy,length,cache):
    if (cx,cy) not in cache:
        if 0 <= cx < length and 0 <= cy < length:
            return True
    return False
    
def bfs(cache, matrix, start, areas):
    length = len(matrix)
    unseenNodes = [start]
    areas[start] = []

    while unseenNodes:
        x,y = unseenNodes.pop()
        for cx,cy in (x+1,y), (x-1,y), (x,y+1), (x, y-1):
            if safe(cx,cy,length,cache) and matrix[cx][cy]== matrix[x][y]:
                cache.append((cx,cy))
                unseenNodes.append((cx,cy))
                areas[start].append((cx,cy))
    return cache, areas
print(find_biggest_area(matrix))
#
