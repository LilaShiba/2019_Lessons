def firstMissingPositive(nums):
    hash_map = {}
    for idx, num in enumerate(nums):
        if num > 0:
            hash_map[num] = idx
    
    num = 1
    if num not in hash_map:
        return num
    
    while True:
        if num not in hash_map:
            return num
        num += 1
        
arr = []        
arr1 = [1,2,0]    
arr2 = [3,4,-1,1]

print(firstMissingPositive(arr2))

