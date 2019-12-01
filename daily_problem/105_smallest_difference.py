# Given an array of positive integers, divide the array into two 
# subsets such that the difference between the sum of the subsets 
# is as small as possible.
# 
# For example, given [5, 10, 15, 20, 25], return the sets 
# {10, 25} and {5, 15, 20}, which has a difference of 5, 
# which is the smallest possible difference.
#arr = [5, 10, 15, 20, 25]
import random
arr = [random.randint(0,100) for x in range(25)]

def smallest_difference_sad(arr):
    arr = sorted(arr,reverse=False)
    a = set()
    b = set()
    n = sum(arr)//2
    
    for num in arr:
        if sum(a) > sum(b):
            b.add(num)
        else:
            a.add(num)
    return (n, sum(a)-sum(b), sum(a),sum(b))
        

def small_backtracking(arr):
    target = sum(arr)//2
    current_est, best_yet = 0, 0
    ans, ans2 = [],[]
    best_ans, best_ans2 = [], []
    n = len(arr)
    arr = sorted(arr, reverse=True)
    
    def is_safe(total, current_num):
        return total + current_num <= target 
    
    
    for num in arr:
        if is_safe(current_est, num):
            current_est += num
            ans.append(num)
        else:
            ans2.append(num)
        
        
    return (target, sum(ans)-sum(ans2), sum(ans), sum(ans2))


print(smallest_difference_sad(arr))
print(small_backtracking(arr))
        
        
        