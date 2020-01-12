import random, pprint

def make_matrix(n,m):
    matrix = [[random.randint(0,10) for x in range(n)]for y in range(m)]

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] > 6:
                matrix[x][y] = 1
            else:
                matrix[x][y] = 0

    pprint.pprint(matrix) 
    return matrix
       
def matrix_to_adj(matrix):
    adj_list = {}
    
    for row in range(len(matrix)):
        adj_list[row] = []
        for col in range(len(matrix[row])):
            if matrix[row][col] > 0:
                adj_list[row].append(col)
    return adj_list

matrix = make_matrix(5,5)            
adj_list = matrix_to_adj(matrix)
print(adj_list)


def backtracking(adj_list, magic_num, ans=[]):
    if len(ans) == len(adj_list):
        return True, ans
    for itr in range(magic_num):
        ans.append(itr)
        if is_safe(adj_list, ans):
            if backtracking(adj_list, magic_num, ans):
                return True, ans
        ans.pop()
    return False, ans
    
def is_safe(adj_list, ans):
    last_iter = ans[-1]
    last_edge = len(ans)-1
    
    neighbors_to_check = [edge for edge in adj_list[last_edge] if edge < last_edge ]
    for edge in neighbors_to_check:
        if ans[edge] == last_iter:
            return False
    return True


def backtrack(adj_list, magic_num, ans=[]):
    if len(ans) == len(adj_list):
        return True, ans
        
    for iter in range(magic_num):
        ans.append(iter)
        if is_safe(adj_list, ans):
            if backtrack(adj_list, magic_num, ans):
                return True, ans
        ans.pop()
    return False, ans

def is_safe(adj_list, ans):
    last_edge = len(ans)-1
    last_iter = ans[-1]
    
    neighbors_to_check = [edge for edge in adj_list[last_edge] if edge < last_edge]
    
    for edge in neighbors_to_check:
        if last_iter == ans[edge]:
            return False
    return True

def bt(adj_list, magic_num, ans=[]):
    if len(adj_list) == len(ans):
        return True, ans
        
    for iter in range(magic_num):
        ans.append(iter)
        if iSafe(adj_list, ans):
            if bt(adj_list, magic_num, ans):
                return True, ans
        ans.pop()
    return False

def iSafe(adj_list, ans):
    last_edge = len(ans)-1
    last_iter = ans[-1]
    neighbors_to_check = [edge for edge in adj_list[last_edge] if edge < last_edge]
    
    for edge in neighbors_to_check:
        if edge == last_iter:
            return False
    return True
    
print(backtracking(adj_list, 2))
print(backtrack(adj_list,2))
print(bt(adj_list, 2))