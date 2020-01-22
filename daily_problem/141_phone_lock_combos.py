def all_combos(arr):
    # end case 
    if len(arr) == 0:
        return [[]]
    # iterate for all in arr
    result = all_combos(arr[1:])
    # every number combo with the first number in arr
    return result + [subarr + [arr[0]] for subarr in result]


def mapping_combos(items, ans):
    if len(items) == 0:
        return [[]]
    
    
    result = mapping_combos(items[1:], ans)
    
    for subarr in result:
        result = result + [subarr + [items[0]]]
            # if is_safe(x,y,ans):
    return result




items = [x+1 for x in range(9)]  
#print(items)  
def make_keys(row,col):
    keys = []
    c = 0
    for x in range(row):
        new_arr = []
        for y in range(col):
            c+=1
            new_arr.append(c)
        keys.append(new_arr)
    return keys

#keys = make_keys(3,3)
#print(keys)


print(mapping_combos(items, []))
