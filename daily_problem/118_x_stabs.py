# This problem was asked by Microsoft.
# 
# Let X be a set of n intervals on the real line. 
# We say that a set of points P "stabs" X if every interval in X 
# contains at least one point in P. Compute the smallest set of points that stabs X.
# 
# For example, given the intervals 
import random,time
t1 = [(1, 4), (4, 5), (7, 9), (9, 12)] 
a1 = [4, 9]

t2 = [ ( random.randint(0,10), random.randint(8,20) ) for x in range(10)]

   

def x_stabs(arr):
    if not arr:
        return []
    arr.sort(key = lambda x: x[1])
    s= arr[0][1]
    
    
    new_arr = []
    
    for x in range(len(arr)):
        if arr[x][0] > s:
            new_arr.append(arr[x])
    
    if not new_arr:
        return s
    e = new_arr[0][1]
    ee = new_arr[0][0]
    
    for x in range(len(new_arr)):
        if new_arr[x][0] <= e and new_arr[x][0] >= ee:
            pass
        else:
            return False
    return s,e
    
def log_time(arr):
    arr.sort(key=lambda x: x[1])
    ans = []
    latest_endpoint = float('-inf')
    print(arr)
    
    for x,y in arr:
        if x <= latest_endpoint:
            continue
        else:
            ans.append(y)
            latest_endpoint = y
    return ans
    
        
start = time.time()    
print(x_stabs(t2))
end = time.time()
time_taken = end - start
print('Time: ',time_taken)

start = time.time()
print(log_time(t2))
end = time.time()
time_taken = end - start
print('Time: ',time_taken)


    