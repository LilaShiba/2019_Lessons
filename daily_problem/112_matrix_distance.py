# This problem was asked by Google.
# 
# Let A be an N by M matrix in which every row and every column is sorted.
# 
# Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].
# 
# For example, given the following matrix:
# 
matrix = [
    [1, 3, 7, 10, 15, 20],
    [2, 6, 9, 14, 22, 25],
    [3, 8, 10, 15, 25, 30],
    [10, 11, 12, 23, 30, 35],
    [20, 25, 30, 35, 40, 45]
    ]
# And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.

def check(matrix, smaller, larger):
    small = large = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] < smaller:
                small += 1
            elif matrix[row][col] > larger:
                large += 1
    return small + large
    
                
def how_many_smaller(matrix, start, end):
    r = len(matrix[0])

    
print(check(matrix,6,23))
print(check_l(matrix, 6, 23))
#print(how_many_smaller(matrix, (0,0), (2,3)))