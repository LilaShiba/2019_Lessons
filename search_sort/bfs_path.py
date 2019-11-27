import random, pprint

def make_maze(n,m):
    maze = [[random.randint(0,10) for x in range(m)]for y in range(n)]
    return maze




def bfs(maze,start,end):
    def is_safe(x,y):
        if (x,y) not in visited:
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
                return True
        return False

    queue = [[start]]
    visited = [(start)]
    
    while queue:
        # first item
        path = queue.pop(0)
        node = path[-1]
        
        if node == end:
            return path
            
        x,y = node

        for cx,cy in (x+1, y), (x-1,y), (x,y-1), (x,y+1):
            if is_safe(cx,cy):
                new_path = list(path)
                new_path.append((cx,cy))
                print(new_path)
                queue.append(new_path)
                visited.append((cx,cy))            
        
    return False


maze = make_maze(5,5)
print(bfs(maze,(0,0), (3,3)))