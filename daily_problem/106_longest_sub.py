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
    
def longest_substring2(arr):
    cache = {}
    start_idx = 0
    longest = 0
    
    for idx, num in enumerate(arr):
        # check cache
        if num in cache:
            if cache[num] >= start_idx:
                longest = max(longest, idx - start_idx)
                start_idx = cache[num] +1
        cache[num] = idx
    return longest, (len(arr)-start_idx)
    
def longest_substring3(arr):
    cache = {}
    start_idx = 0
    result = 0
    
    for idx, num in enumerate(arr):
        # check cache
        if num in cache:
            if cache[num] >= start_idx:
                result = max(result, idx - start_idx )
                start_idx = cache[num] +1
        cache[num] = idx
                
            
    return (max(result, len(arr)-start_idx))
    
def kadane_remix(arr):
    current, best = [], []
    
    for num in arr:
        if num not in current: 
            current.append(num)
        else:
            current = [num]
        
        if len(current) > len(best): 
            best = current
    return best
        

print(longest_substring2(arr))
print(longest_substring3(arr))
print(kadane_remix(arr))