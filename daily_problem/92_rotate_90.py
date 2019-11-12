import random, pprint

def make_matrix(n):
    return [[random.randint(0,100)for x in range(n)]for y in range(n)]

def rotate_90(matrix):
    n = len(matrix)
    ans = [[0 for x in range(n)]for y in range(n)]
    for x in range(n):
        for y in range(n):
            ans[y][n-x-1] = matrix[x][y]
    return ans
    
def ans(matrix):
    n = len(matrix)
    ans = [[0 for x in range(n)]for y in range(n)]
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            ans[c][n-r-1] = val
    return ans
matrix = make_matrix(100)
ans1 = rotate_90(matrix)
ans2 = ans(matrix)
print(ans1 == ans2)