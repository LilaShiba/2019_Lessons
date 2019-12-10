# This problem was asked by Facebook.
# 
# Suppose you are given two lists of n points, one list p1, p2, ..., 
# pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. 
# Imagine a set of n line segments connecting each point pi to qi. 
# Write an algorithm to determine how many pairs of the line segments intersect.

def intersect(l1, l2):
    return (l1[0] < l2[0] and li[1] > l2[1] ) or (l1[0] < l2[0] and l1[1] < l2[1] )

def num_intersections(lst1, lst2):
    lines = zip(lst1, lst2)
    count = 0
    for i, l1 in enumerate(lines):
        for l2 in lines[i+1]:
            if intersect(l1, l2):
                count += 1
    return count
    
