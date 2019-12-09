boxes = [
     {
        "top_left": (1, 4),
        "dimensions": (3, 3) # width, height
    },
    {
        "top_left": (-1, 3),
        "dimensions": (2, 1)
    },
    {
        "top_left": (0, 5),
        "dimensions": (4, 3)
    }
]

def check_all(boxes):
    for i, rect1 in enumerate(boxes):
        for rect2 in boxes[i + 1:]:
            if overlap(rect1, rect2):
                return True
    return False
    

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
        return False
    
    return(right_x -  left_x) * (top_y - bottom_y)
    
print(check_all(boxes))
    