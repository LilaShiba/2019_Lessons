# This problem was asked by Uber.
# 
# Suppose an array sorted in ascending order 
# is rotated at some pivot unknown to you beforehand. 
# Find the minimum element in O(log N) time. 
# You may assume the array does not contain duplicates.
# 
# For example, given [5, 7, 10, 3, 4], return 3.

def merge_sort(arr):
    if len(arr) > 1:
        
        n = len(arr)
        mid = n//2
        l = arr[:mid]
        r = arr[mid:]
        merge_sort(l)
        merge_sort(r)
        
        i=j=k=0
        
        while i < len(l) and j < len(r):
            if l[i] > r[j]:
                arr[k] = r[j]
                j+=1
            else:
                arr[k] = l[i]
                i += 1
            k+=1
        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while j < len(r):
            arr[k]= r[j]
            j+=1
            k+=1
    return arr[0]
        
        
arr = [5, 7, 10, 3, 4]
print(merge_sort(arr))