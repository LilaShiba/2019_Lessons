def iterative_binary_search(arr,x):
    low,high = 0, len(arr)-1
    
    while low <= high:
        mid = (low +  high)//2
        if arr[mid] == x:
            print('target is at idx',mid)
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False
    
print(iterative_binary_search([12,15,16,18,20],20))
print(iterative_binary_search([n = [5, 1, 2, 7, 3, 4], 4))