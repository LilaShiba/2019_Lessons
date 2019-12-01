# This problem was asked by Google.
# 
# Given two rectangles on a 2D graph, return the area of their 
# intersection. If the rectangles don't intersect, return 0.
# 
# For example, given the following rectangles:
# 

rect1 = {
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}

# and


rect2 = {
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
# return 6


def overlap(rect1, rect2):
    left_x = max(rect1['top_left'][0], rect2['top_left'][0])
    #print(left_x)
    right_x = min(rect1['top_left'][0] + rect1['dimensions'][0], rect2['top_left'][0] + rect2['dimensions'][0] )
    #print(right_x)
    top_y = min(rect1['top_left'][1], rect2['top_left'][1])
    #print(top_y)
    bottom_y = max(rect1['top_left'][1] - rect1['dimensions'][1], rect2['top_left'][1] - rect2['dimensions'][1] )
    #print(bottom_y)
    if left_x > right_x or bottom_y > top_y:
        return 0
    
    return(right_x -  left_x) * (top_y - bottom_y)

def intersect_r(rect1, rect2):
    left_x = max(rect1['top_left'][0], rect2['top_left'][0])
    #print(top_left)
    right_x = min(rect1['top_left'][0]+rect1['dimensions'][0],rect2['top_left'][0] + rect2['dimensions'][0])
    #print(top_right)
    top_y = min(rect1['top_left'][1], rect2['top_left'][1])
    bottom_y = max(rect1['top_left'][1] - rect1['dimensions'][1], rect2['top_left'][1] - rect2['dimensions'][1]) 
    #print(top_y)
    #print(bottom_y)
    
    # if overlap
    if left_x > right_x or bottom_y > top_y:
        return 0
    # other wise
    return (right_x - left_x) * (top_y-bottom_y)
print(overlap(rect1,rect2))
print(intersect_r(rect1, rect2))