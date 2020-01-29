# This problem was asked by Yelp.
# 
# You are given an array of integers, where each element represents 
# the maximum number of steps that can be jumped going forward from 
# that element. Write a function to return the minimum number of jumps 
# you must take in order to get from the start to the end of the array.
# 
# For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, 
# as the optimal solution involves jumping from 6 to 5, and then from 5 to 9

import random
#n = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]

n = [random.randint(3,10) for x in range(230)]
def can_make_to_end(arr):
    furthest = 0
    
    for idx, int in enumerate(arr):
        
        if idx > furthest:
            break
        
        furthest = max(furthest, int+idx)
    return furthest > len(arr)-1
        



def dp_least_jumps(arr):
    n = len(arr)
    jumps = [0 for x in range(n)]    
    
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if arr[j] != float('inf') and i <= j + arr[j]:
                jumps[i] = min(jumps[i], jumps[j]+1)
                break
    return jumps[-1]
    
def linear_least_jumps(arr):
    jumps = 1
    ladder = arr[0]
    stairs = arr[0]
    n = len(arr)
    
    for x in range(1, n):
        # end case
        if n-1 == x:
            return jumps
        
        # update ladder 
        ladder = max(ladder, x + arr[x])
        stairs -= 1
        # if stairs run out
        if stairs == 0:
            jumps += 1
            if x >= ladder:
                return -1
            
            stairs = ladder - x
        
        
    
print(can_make_to_end(n))
print(dp_least_jumps(n))
print(linear_least_jumps(n))