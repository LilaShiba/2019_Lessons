# find the min and max of a list 
# using less than 2 * (n-2) compare


arr = [4,9,2,10,-1,14,8]

def find_min_max(arr):
    min_arr = max_arr = arr[0]
    
    compare = lambda x,y: (x,y) if y > x else (y,x)
    
    # make odd for pair compare
    if len(arr) % 2 == 0:
        arr.append(arr[-1])
    
    for i in range(1, len(arr), 2):
        small, big = compare(arr[i], arr[i+1])
        min_arr = min(small, min_arr)
        max_arr = max(big, max_arr)
    return min_arr, max_arr

def r_min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]    
    elif len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
    else:
        n = len(arr)//2
        l_min, l_max = r_min_max(arr[:n])
        r_min, r_max = r_min_max(arr[n:])
        return min (l_min, r_min), max(l_max, r_max)
    
print(find_min_max(arr))
print(r_min_max(arr))