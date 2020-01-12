# This problem was asked by Twitter.
# 
# Given a list of numbers, create an algorithm that arranges 
# them in order to form the largest possible integer. 
# For example, given [10, 7, 76, 415], you should return 77641510

arr = [10, 7, 76, 415]
ans = 77641510

def make_best(arr):
    nums = [str(x) for x in arr]
    nums = ''.join(nums)
    nums = [int(x) for x in nums]
    hi = merge_sort(nums)
    hi = [str(x) for x in hi]
    hi = int("".join(hi))
    
    print(hi)
    return hi

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        r = arr[:mid]
        l = arr[mid:]
        
        merge_sort(r)
        merge_sort(l)
        
        i=j=k=0
        
        while i < len(r) and j < len(l):
            if r[i] > l[j]:
                arr[k] = r[i]
                i += 1
            else:
                arr[k] = l[j]
                j += 1
            k += 1
        
        while i < len(r):
            arr[k] = r[i]
            i += 1
            k += 1
        while j < len(l):
            arr[k] = l[j]
            j += 1
            k += 1
    return arr
        
#hi = make_best(arr)


def make_hi(arr):
    arr = [str(x) for x in arr]
    arr = [list(x) for x in arr]
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            arr[x][y] = int(arr[x][y])
            
    # after making each int a set
    arr = sorted(arr, key = lambda x:x[0], reverse= True)
    print(arr)
    ans = ''
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            ans += str(arr[x][y])
    return int("".join(ans))
            

hi = (make_hi(arr))
print(hi == ans)