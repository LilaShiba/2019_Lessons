# This problem was asked by Amazon.
# 
# Given a sorted array, find the smallest positive integer that 
# is not the sum of a subset of the array.
# 
# For example, for the input [1, 2, 3, 10], 
# you should return 7.
# 
# Do this in O(N) time.

arr = [1, 2, 3, 10]

def sm(arr):
    res = 1
    n = len(arr)-1
    for i in range(0, n):
        if arr[i] <= res:
            res = res + arr[i]
        else:
            break
    return res
    
print(sm(arr))
    