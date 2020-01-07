import random, pprint

class Graph:
    def __init__(self,v):
        self.v = len(v)
        self.graph = v
    
    def make_matrix(self, v):
        n = range(len(v))
        maze = [[0 for x in n] for y in n]
        
        for x,y in v.items():
            for items in y:
                maze[x][items] = 1
                maze[items][x] = 1
        self.graph = maze
        return maze
        
    def show_graph(self):
        pprint.pprint(self.graph)
        

def house_colors(adj_list, magic_num, colors=[]):
    # end case
    if len(colors) == len(adj_list):
        return True, colors
    # try each option for every single house
    for i in range(magic_num):
        colors.append(i)
        # check to see conditions are met
        if is_safe(adj_list, colors):
            # driver code via recursion
            if house_colors(adj_list, magic_num, colors):
                return True, colors
        colors.pop()
    return False

def is_safe(adj_list, colors):
    last_color = colors[-1]
    last_vertex = len(colors)-1
    
    neighbors = [x for x in adj_list[last_vertex] if x < last_vertex]
    
    for edge in neighbors:
        if colors[edge] == last_color:
            return False
    return True


adj_list = {
0: [1],
1: [2],
2: [3,1],
3: [4],
4: [5],
5: [0]
}

print(house_colors(adj_list,2,))