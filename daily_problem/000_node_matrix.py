import random, pprint
import heapq


class Node:
    def __init__(self,v):
        self.v = v
        self.parent = None
        self.visited = False
        self.cost = v
        
class Matrix:
    def __init__(self,x,y):
        self.col = x
        self.row = y
        self.matrix = [[Node(random.randint(0,10)) for col in range(x)]for _ in range(y)]
        self.matrix[0][0].v = self.matrix[-1][-1].v = 0

    def print_matrix(self):
        pprint.pprint([[col.v for col in x]for x in self.matrix])

    def bfs(self,start=(0,0), end=None, params=None):
        queue = []
        queue.append([start])
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            x,y = node
            if (x, y) == end:
                print(True, path)
                return True, path
            if self.matrix[x][y].visited == False:
                self.matrix[x][y].visited = True
                for cx, cy in (x+1, y), (x-1, y), (x, y-1), (x, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1):
                    if 0<= cx <= self.row-1 and 0 <= cy < self.col:
                        if self.matrix[cx][cy].v < params:
                            new_path = list(path)
                            new_path.append((cx,cy))
                            queue.append(new_path)
        print(False)
        return False
    
    def astar(self, start=(0,0,0,0), end=None):
        unseenNodes = [start]
        heapq.heapify(unseenNodes)
        visited = {(0,0):0}
        
        while unseenNodes:
            minNode = heapq.heappop(unseenNodes)
            distance,current_weight,x,y = minNode
            px,py = x,y
            
            neighbors = ((x-1, y), (x+1, y), (x, y-1), (x, y+1))
            real_neighbors = ((x,y) for (x,y) in neighbors if 0<= x < self.row and 0<= y < self.col)
            
            for cx,cy in real_neighbors:
                cost = current_weight + self.matrix[cx][cy].v
                dist = abs(end[0]-cx) + abs(end[1]-cy)
                if (cx,cy) not in visited or cost < visited[(cx,cy)]:
                    visited[(cx,cy)] = cost
                    self.matrix[cx][cy].parent = (px,py)
                    heapq.heappush(unseenNodes, (dist,cost,cx,cy))
                    if (cx,cy) == end:
                        print(visited[cx,cy])
                        return(visited[cx,cy])
        print("False")
            
        
    
    def dijkstra(self, start=(0,0,0), end=None, params=None):
        unseenNodes = [start]
        visited = {(0,0): 0}
        parent = {}
        
        while unseenNodes:
            unseenNodes = sorted(unseenNodes, key = lambda x:x[2])
            minNode = unseenNodes.pop(0)
            x,y,current_weight = minNode
            # end case
            if (x,y) == end:
                print("True")
                print(self.matrix[x][y].cost)
                return(self.matrix[x][y].cost)
            # copy parents
            px,py = x,y
            # get directions within bounds
            neighbors = ((x-1, y), (x+1, y), (x, y-1), (x, y+1))
            real_neighbors = ((x,y) for (x,y) in neighbors if 0<= x < self.row and 0<= y < self.col)
            
            for cx,cy in real_neighbors:
                cost = current_weight + self.matrix[cx][cy].v
                if self.matrix[cx][cy].visited == False or cost < self.matrix[cx][cy].cost:
                    self.matrix[cx][cy].visited = True
                    self.matrix[cx][cy].cost = cost
                    self.matrix[cx][cy].parent = (x,y)
                    unseenNodes.append((cx,cy,cost))
        print("False")
            
        
             
maze = Matrix(5,5)
maze.print_matrix()
#maze.bfs((0,0), (4,4), 1)
maze.dijkstra((0,0,0), (2,2))
maze.astar((0,0,0,0), (2,2))