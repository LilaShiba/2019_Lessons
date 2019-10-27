# Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, 
# replace the color of the given pixel and all adjacent same colored pixels with C.
# 
# For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:
# 
# B B W
# W W W
# W W W
# B B B
# Becomes
# 
# B B G
# G G G
# G G G
# B B B
import random, pprint

def create_matrix_rgb(row_size, col_size):
    colors = ['R', 'G', 'B']
    matrix = []
    for row in range(row_size):
        matrix.append([])
        for col in range(col_size):
            matrix[row].append(colors[random.randint(0,2)])
    return matrix

def replace_adj_pixl(node, matrix, change_color):
    colors = ['R', 'G', 'B', '*']

    queue = [node]
    explored = []
    color = matrix[node[0]][node[1]]
    
    while queue:
        x,y = queue.pop()
        for cx,cy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if is_safe((cx,cy), matrix, color):
                if (cx, cy) not in explored:
                    explored.append( (cx,cy) ) 
                    queue.append( (cx,cy) )
    
    for node in explored:
        x,y = node 
        matrix[x][y] = colors[change_color]
        
    return explored, matrix
                    
# in maze and is color
def is_safe(child, matrix, color):
    x,y = child
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
        if matrix[x][y] == color:
            return True 
    return False 
        
    
    
matrix = create_matrix_rgb(5,5)
pprint.pprint(matrix)
pprint.pprint(replace_adj_pixl((0,0), matrix, 3))   
    