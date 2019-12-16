# This problem was asked by Google.
# 
# You are given an array of arrays of integers, 
# where each array corresponds to a row in a triangle of numbers.
#  For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:
# 
#   1
#  2 3
# 1 5 1
#
# We define a path in the triangle to start at the top 
# and go down one row at a time to an adjacent value, 
# eventually ending with an entry on the bottom row. 
# For example, 1 -> 3 -> 5. The weight of the path 
# is the sum of the entries.
# 
# Write a program that returns the weight 
# of the maximum weight path.

import node


def heavy_path(node):
    if not node:
        return 0
    l = node.v + heavy_path(node.l)
    r  = node.v + heavy_path(node.r)
    return max(l,r)


root = node.Node(5)
root.l = node.Node(4)
root.r = node.Node(6)
root.r.r = node.Node(8)
root.r.l = node.Node(6)
root.l.l = node.Node(2)
root.l.l = node.Node(1)
print(heavy_path(root))

def arr_heavy_path(arr,lvl=0,idx=0):
    if lvl == len(arr)-1:
        return arr[lvl][idx]
    else:
        return arr[lvl][idx] + max(arr_heavy_path(arr,lvl+1,idx), arr_heavy_path(arr, lvl+1, idx+1))


        
arr1 = [
[1],
[2,3],
[1,5,1]
]

print(arr_heavy_path(arr1))




