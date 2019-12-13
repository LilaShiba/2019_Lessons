# This problem was asked by Amazon.
# 
# Given an array and a number k that's smaller than the 
# length of the array, rotate the array to the right k elements in-place.

def rotate(arr, k):
    n = len(arr)
    turns = 0
    while turns < k:
        num = arr.pop(0)
        arr.append(num)
        turns += 1
    return arr

def slice(arr,k):
    n = len(arr)-k
    return arr[:n] + arr[n:]
    
arr = [1,2,3,4,5]
k = 3
print(rotate(arr, k))
print(slice(arr,k))