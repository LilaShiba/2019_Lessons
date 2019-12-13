# This problem was asked by Google.
# 
# Given a set of distinct positive integers, 
# find the largest subset such that every pair of elements in the subset (i, j) 
# satisfies either i % j = 0 or j % i = 0.
# For example, given the set 
import random 
arr = [3, 5, 10, 20, 21] 
ans = [5, 10, 20]
arr2 = [1, 3, 6, 24]
ans2 = [1, 3, 6, 24]
arr3 = [random.randint(1,100) for x in range(20)]

def lset(arr):
    def isafe(s1,s2):
        return s1 % s2 == 0 or s2 % s1 == 0
    current = best = []
    
    for idx in range(1, len(arr)):
        if isafe(arr[idx-1], arr[idx]):
            current.append((arr[idx-1], arr[idx]))
            best = max(best, current)
        else:
            current = []
    ans = []
    for x,y in best:
        if x not in ans:
            ans.append(x)
        if y not in ans:
            ans.append(y)
            
        
    return ans
        
#print(lset(arr))

def dplset(arr):
    if not arr:
        return []
    n = len(arr)
    nums = sorted(arr)
    dp = [[nums[x]] for x in range(n)]
    
    max_len, ans = 1, dp[0]
    
    for i in range(1, n):
        for j in range(i):
            # if i%j = 0 and num j is the best num to divide with because it produces the most
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j])+1:
                # add j and i to the list
                dp[i] = dp[j] + [nums[i]]
                # if row has more ints in it
                if len(dp[i]) > max_len:
                    # set it as best
                    max_len, ans = len(dp[i]), dp[i]
    return ans
    
def dp(arr):
    # no arr case
    if not arr:
        return []
    n = len(arr)
    arr = sorted(arr)
    cache = [[arr[x]]for x in range(n)]
    ans = []
    max_len = 0
    for i in range(1,n):
        for j in range(i):
            if arr[i]%arr[j] == 0 and len(cache[i]) < len(cache[j]) + 1:
                cache[i] = [arr[i]] + cache[j]
                if len(cache[i]) > max_len:
                    max_len, ans = len(cache[i]), cache[i]
    return ans 
print(dplset(arr3))
print(dp(arr3))
        