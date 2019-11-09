# This problem was asked by Amazon.
#
# Given a pivot x, and a list lst, partition the list into three parts.
#
# The first part contains all elements in lst that are less than x
# The second part contains all elements in lst that are equal to x
# The third part contains all elements in lst that are larger than x
# Ordering within a part can be arbitrary.
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
