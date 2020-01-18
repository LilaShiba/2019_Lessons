def all_combos(arr):
    if len(arr) == 0:
        return [[]]
    
    result = all_combos(arr[1:])
    return result + [subarr + [arr[0]] for subarr in result]


def all_mapping_combos(items, mapping):
    item = items[0]

    if len(items) == 1:
        return mapping[item]
    
    ans = []
    
    for x in mapping[item]:
        for y in all_mapping_combos(items[1:], mapping):
            ans.append(y+x)
    return ans 
    

def combos(arr):
    if len(arr) == 0:
        return [[]]
    result = combos(arr[1:])
    return result + [subarray + [arr[0]] for subarray in result]





    
if __name__ == '__main__':
    mapping = {'1': ['a','b','c'], '2':['d','e','f'], '3':['h','i','j']}
    # print(all_mapping_combos(['1','2','3'], mapping))
    print(all_combos([1,2,3]))
    # print(combos([1,2,3]))
