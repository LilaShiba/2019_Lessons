# This problem was asked by Bloomberg.
# 
# There are N prisoners standing in a circle, waiting to be executed. 
# The executions are carried out starting with the kth person, and 
# removing every successive kth person going clockwise until there is no one left.
# 
# Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.
# 
# For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.
# 
# Bonus: Find an O(log N) solution if k = 2.

people = 5
pattern = 2

def best_spot(n,k):
    if n == 1:
        return 1
    else:
        return (best_spot(n-1, k) +k-1) % n+1
        
        
    
    print(arr)

def best_spot2(n,k):
    r = 0
    for i in range(1, n+1):
        r = (r+k)%i
    return r
        
        
        
        

print(best_spot(5,2))

print(best_spot2(5,2))

# 
# After the first person (kth from beginning) is killed, n-1 persons are left. 
# So we call josephus(n – 1, k) to get the position with n-1 persons. But 
# the position returned by josephus(n – 1, k) will consider the position 
# starting from k%n + 1. So, we must make adjustments to the position returned 
# by josephus(n – 1, k).
# 
# Following is simple recursive implementation of the Josephus problem. 
# The implementation simply follows the recursive structure mentioned above.        