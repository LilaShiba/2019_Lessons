arr = [1,2,3]

def all_perms(arr):
    if len(arr) == 1:
        return [arr]
    
    ans = []
    for int in range(len(arr)):
        temp = arr[:int] + arr[int+1:]
        current = arr[int]
        for perms in all_perms(temp):
            print(perms)
            ans.append([current] + perms)
    return ans

def ap(arr):
    ans = []
    if len(arr) == 1:
        return [arr]
    for x in range(len(arr)):    
        current = arr[x]
        temp = arr[:x] + arr[x+1:]
        for perm in ap(temp):
            ans.append([current]+perm)
    return ans
        
print(all_perms(arr))
print(ap(arr))
            
        