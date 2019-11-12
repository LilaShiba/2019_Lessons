# This problem was asked by Google.
# 
# Given an array of integers, return a new array where each element in 
# the new array is the number of smaller elements to the right of that element 
# in the original input array.
# 
# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:
# 
# There is 1 smaller element to the right of 3
# There is 1 smaller element to the right of 4
# There are 2 smaller elements to the right of 9
# There is 1 smaller element to the right of 6
# There are no smaller elements to the right of 1
import bisect

def naive(lst):
    ans = []
    for num in range(len(lst)):
        right = lst[num+1:]
        current_num = lst[num]
        count = 0
        for next_num in right:
            if next_num < current_num:
                count += 1
        ans.append(count)
    return ans
    
def naive1(lst):
    ans = []
    n = range(len(lst))
    for num in n:
        count = 0
        current_num = lst[num]
        for next_num in lst[num+1:]:
            if next_num < current_num:
                count += 1
        ans.append(count)
    return ans

def bisect_shorter_than(lst):
    ans = []
    s = []
    for num in reversed(lst):
        i = bisect.bisect_left(s,num)
        ans.append(i)
        bisect.insort(s, num)       
    return list(reversed(ans))
    
    
import random
test1 = [random.randint(0,1000) for num in range(10)]        
arr = [3, 4, 9, 6, 1]  
print(bisect_shorter_than(test1))   
print(naive1(test1))   