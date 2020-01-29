# O(n*k)
def max_sub(arr,k):
    for x in range(len(arr)-k+1):
        return(max(arr[x:x+k]))

arr = [10,-5,-12,7,8,7]
print(max_sub(arr,3))



def kadens(arr):
    current = best = 0
    for x in arr:
        current = max(x, current+x)
        best = max(current, best)
    return best

print(kadens(arr))