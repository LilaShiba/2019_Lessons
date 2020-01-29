# This problem was asked by Etsy.
# 
# Given an array of numbers N and an integer k, 
# your task is to split N into k partitions such 
# that the maximum sum of any partition is minimized. 
# Return this sum.
# 
# For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, 
# you should return 8, since the optimal partition is 
# [5, 1, 2], [7], [3, 4]
import random
n = [random.randint(0,100) for x in range(10)]  
k = 3
 
def min_sum(arr, subarr):
    new_arr = sorted(arr)
    ans = new_arr[-1]
    sub_arr = new_arr[:-1]
    while sum(sub_arr)//2 >= ans:
        node = sub_arr.pop(0)
        ans+=node
    return ans

# We could proceed by checking each value between 
# the maximum element and the array sum until finding 
# the smallest one that works. A more efficient way, 
# however, would be to perform a binary search.    

def p_sum(arr, subarr):
    arr=sorted(arr)
    left, right = max(arr), sum(arr)   
    
    while left < right:
        mid = (left+right)//2
        
        if can_p(arr, mid, subarr):
            right = mid
        else:
            left = mid + 1  
    return left  
        
    

def b_search(arr,target):
    left, right = 0, len(arr)-1
    
    while left <= right:
        mid = (left+right)//2
        
        if arr[mid] == target:
            print('Target is at idx:', mid)
            return True, mid
        
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
    
    
def max_partition_sum(array, k):
    array = sorted(array)
    left, right = max(array), sum(array)

    while left < right:
        mid = (left + right) // 2
        # if you can split the array more
        # do so by taking off the high nums
        if can_partition(array, mid, k):
            right = mid
        else:
            # if you can't partition off the ints
            # you must add it to your total ans
            left = mid + 1

    return left
    
def can_partition(array, limit, k):
    total = 0
    partitions = 1

    for num in array:
        if total + num > limit:
            total = num
            partitions += 1
            if partitions > k:
                return False
        else:
            total += num

    return True    

def can_p(arr, mid, subarr):
    total = 0
    partition = 1
    
    for int in arr:
        if total + int > mid:
            partition +=1
            total = int 
            if partition > subarr:
                return False
        else:
            total += int
    return True        
        
#print(min_sum(n,k))
print('given ans', max_partition_sum(n,k))
print('p_sum', p_sum(n,k))

