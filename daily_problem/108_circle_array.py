# This problem was asked by Facebook.
# 
# Given a circular array, compute its maximum subarray sum in O(n) time. 
# A subarray can be empty, and in this case the sum is 0.
# 
# For example, given [8, -1, 3, 4], return 15 as we choose the numbers 
# 3, 4, and 8 where the 8 is obtained from wrapping around.

# Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

arr = [2,-4, 5, 1, 0]
arr2 = [2, -1, 3, 2, 4, -5, 10]
# 
# def highest_sub_circle(arr):
#     n, i = len(arr), 0
#     current,highest = 0,0
#     found = False
#     circle_to = None
#     cache = {x:True for x in arr if x < 0}
# 
#     # if all pos
#     # if True not in cache:
#     #     print('wow')
#     #     return sum(arr)
# 
#     while True:
#         if arr[i] > 0:
#             current += arr[i]
#         else:
#             if current > highest:
#                 highest = current
#                 current = 0
#                 if found == False:
#                     found = True
#                     circle_to = i
#         i+=1
#         print(i)
#         # reset circle 
#         if i >= n and circle_to != None:
#             i = 0
#         else:
#             return highest
arr = [2,-4, 1, 5, 0]
def highest_sub_circle(arr):
    def kadane(arr):
        best, current = 0, 0
        for x in arr:
            current = max(x, current+x)
            best = max(best,current)
        return best

def maxSubarraySumCircular(self, A):

    if max(A) <= 0: return max(A)
    endmax = [i for i in A]
    endmin = [i for i in A]
    for i in range(1,len(A)):
        if endmax[i-1] > 0: 
            endmax[i] += endmax[i-1]
        if endmin[i-1] < 0: 
            endmin[i] += endmin[i-1]

    return max(max(endmax),sum(A) - min(endmin))
    

                    
# method 2 merge sort and sum all non 0's    
    
print(kadane(arr))
            
        
        