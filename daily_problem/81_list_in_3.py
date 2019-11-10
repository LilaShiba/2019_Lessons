# This problem was asked by Amazon.
#
# Given a pivot x, and a list lst, partition the list into three parts.
#
# The first part contains all elements in lst that are less than x
# The second part contains all elements in lst that are equal to x
# The third part contains all elements in lst that are larger than x
# Ordering within a part can be arbitrary.
<<<<<<< HEAD
#
# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10],
# one partition may be [9, 3, 5, 10, 10, 12, 14]

# hi => low

def m_sort(arr):
    n = len(arr)
    mid = n//2
    if n > 1:
        l_side = arr[:mid]
        r_side = arr[mid:]
        m_sort(l_side)
        m_sort(r_side)

        i,j,k = 0,0,0

        while i < len(l_side) and j < len(r_side):
            if l_side[i] > r_side[j]:
                arr[k] = l_side[i]
                i += 1
            else:
                arr[k] = r_side[j]
                j += 1
            k+=1

        while i < len(l_side):
            arr[k] = l_side[i]
            i += 1
            k += 1
        while j < len(r_side):
            arr[k] = r_side[j]
            j += 1
            k += 1
        return arr

def s_sort(arr, x):
    
print(m_sort([9, 12, 3, 5, 14, 10, 10]))
=======
# 
# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].

    
def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left_side = arr[mid:]
        right_side = arr[:mid]
        
        merge_sort(left_side)
        merge_sort(right_side)
        
        i = j = k = 0
        
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1
            k += 1
        
        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1
        
        while j < len(right_side):
            arr[k] = right_side[j]
            j += 1
            k += 1
    return arr

arr=[2,56,6,76,3432,2,56,8,6,42,2,1]
print(merge_sort(arr))
print(par3(arr, 76))
>>>>>>> 8ef8ebd7e6c2e967310ccb2014b5b48e4dbb24ea
