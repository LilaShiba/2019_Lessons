#Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.

def sort_p(arr, start, end):
    old_start = arr[:start]
    old_end = arr[end+1:]
    new_list = arr[start:end]
    r_new_list = []
    x = end
    while x > start-1:
        r_new_list.append(arr[x])
        x -= 1
    return old_start + r_new_list + old_end


print(sort_p([1,2,3,4,5],0,3))