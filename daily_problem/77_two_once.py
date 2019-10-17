# given an array of ints where two elements appear excatly once
# return those elements. Can you do this in linear time and constant space?

arr = [2,4,6,8,10,2,6,10,8,1]
# => 4,8

# slow
def find_two(arr):
    cache = {}
    ans = []
    for x in arr:
        if x not in cache:
            cache[x] = 1
        else:
            cache[x] += 1
    for x in cache:
        if cache[x] == 1:
            ans.append(x)
    return ans

def merge_sort(arr, pos):
    # pos if dealing with nested data
    if len(arr) > 1:
        mid = len(arr)//2
        l_half = arr[:mid]
        r_half = arr[mid:]
        
        merge_sort(l_half, pos)
        merge_sort(r_half, pos)
        
        ri,li,p = 0,0,0
        
        while ri < len(r_half) and li < len(l_half):
            if r_half[ri] < l_half[li]:
                arr[p] = r_half[ri]
                ri += 1
            else:
                arr[p] = l_half[li]
                li += 1
            p += 1
        
        while ri < len(r_half):
            arr[p] = r_half[ri]
            ri += 1
            p += 1
        
        while li < len(l_half):
            arr[p] = l_half[li]
            li += 1
            p += 1
    return arr

# only works for our tight problem contraints appearing twice or once
def quick_find(arr):
    arr_s = merge_sort(arr, 0)
    print(arr_s)
    ans = []
    #ans = [arr_s[x] == arr_s[x+1] for x in range(len(arr_s)-1)]
    
    x = 0
    while x < len(arr)-1:
        if arr_s[x] == arr_s[x+1]:
            x += 2
        else:
            ans.append(arr_s[x])
            x += 1
    return ans

        
    
    
print(quick_find(arr))
