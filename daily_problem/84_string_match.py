# Find an efficient algorithm to find the smallest distance 
# (measured in number of words) between any two given words in a string.
# 
# For example, given words "hello", and "world" and a text content of 
# "dog cat hello cat dog dog hello cat world", 
# return 1 because there's only one word "cat" in between the two words.

def find_dist(text, w1, w2):
    text_words = [w.strip() for w in text.split(' ')]
    print("Scanning {} \nfor the distance between {} and {}".format(text_words, w1, w2))
    w1_idx = [i for i, w in enumerate(text_words) if w == w1]
    w2_idx = [i for i, w in enumerate(text_words) if w == w2]
    print("{} list: {}".format(w1, w1_idx))
    print("{} list: {}".format(w2, w2_idx))
    if not w1_idx or not w2_idx:
        return float('inf')
    # set up two indexs
    i = j = 0
    min_dist = abs(w1_idx[i] - w2_idx[j])
    
    while i < len(w1_idx) and j < len(w2_idx):
        current_dist = abs(w1_idx[i] - w2_idx[j])
        min_dist = min(min_dist, current_dist)
        
        # Don't skip numerical order
        if w1_idx[i] < w2_idx[j]:
            i +=1
        else:
            j +=1
    return min_dist - 1
    
    

print(find_dist("dog cat hello cat dog dog hello cat world", "hello", "world"))