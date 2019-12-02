# This is your coding interview problem for today.
# 
# This problem was asked by Google.
# 
# Given an array of elements, return the length of the longest subarray 
# where all its elements are distinct.
# 
# For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], 
# return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
arr = [5, 1, 3, 5, 2, 3, 4, 1]

def longest_substring(arr):
    if not arr: 
        return arr
    
    n = len(arr)-1
    res,best = [],[]
    
    for i in range(n):
        j = i + 1
        res = []

        while j <= n:
            if arr[j] not in res:
                res = arr[i:j+1]
                j += 1
            else:
                break
        
        if len(res) > len(best):
            best=res 
    
    return best

print(longest_substring(arr))