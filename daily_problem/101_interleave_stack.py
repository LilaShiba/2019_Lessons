# This problem was asked by Google.
# 
# Given a stack of N elements, interleave the first half of the 
# stack with the second half reversed using only one other queue. 
# This should be done in-place.
# 
# Recall that you can only push or pop from a stack, 
# and enqueue or dequeue from a queue.
# 
# For example, if the stack is [1, 2, 3, 4, 5], it should become 
# [1, 5, 2, 4, 3]. 
# If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].


stack = [1, 2, 3, 4, 5]
ans = [1, 5, 2, 4, 3]
stack2 = [1, 2, 3, 4]


def interleave(stack):
    n = len(stack)//2
    arr = stack[n:]
    arr = arr[::-1]
    ans = []
    counta = 0
    counts = 0
    for x in range(len(stack)):
        if x % 2 == 0:
            ans.append(stack[counts])
            counts += 1
        else:
            ans.append(arr[counta])
            counta += 1
    return ans
    
    
    
print(interleave(stack2))

        