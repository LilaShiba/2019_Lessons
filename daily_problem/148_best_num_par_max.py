# This problem was asked by Etsy.
# 
# Given an array of numbers N and an integer k, 
# your task is to split N into k partitions such 
# that the maximum sum of any partition is maximumized. 
# Return this sum.
# 
# For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, 
# you should return 8, since the optimal partition is 
# [5, 1, 2], [7], [3, 4]'

n = [x+1 for x in range(12)]
k = 4
ans = 3

def max_sub(arr, k):
    low, hi = min(arr), sum(arr)
    
    while low < hi:
        mid = (low+hi)//2
        if can_p(arr, mid, k):
            hi = mid
        else:
            low = mid + 1
            
    return hi
    
def can_p(arr,mid,k) -> bool:
    total = 0
    partitions = 1
    
    for int in arr:
        if int + total > mid:
            total = int 
            partitions += 1
            if partitions > k:
                return False
        else:
            total += int
    return True
    
#print(max_sub(n,k))


def min_sub(arr,k):
    left,right=max(arr),sum(arr)
    
    while left < right:
        mid = (left+right)//2
        if can_partition(arr, mid, k):
            right = mid
        else:
            left = mid + 1
    return left

def can_partition(arr: list, limit: int, p_limit: int) -> bool:
    total=partition=0
    for num in arr:
        if total+num > limit:
            total = num
            partition+=1
            if partition > p_limit:
                return False
        else:
            total += num
    return True

def minSub(arr, k):
    arr = sorted(arr)
    left, right = max(arr), sum(arr)
    
    while left < right:
        mid = (left+right)//2
        if can_make_less(arr, mid, k):
            right = mid
        else:
            left = mid + 1
    return left
    
def can_make_less(arr, limit, p_limit):
    partitions = current_sum = 0
    
    for x in arr:
        if x + current_sum > limit:
            current_sum = x 
            partitions += 1
            if partitions > p_limit:
                return False
        else:
            current_sum += x
    return True
    
    
print(min_sub(n,k))
print(minSub(n,k))