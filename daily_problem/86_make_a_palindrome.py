# This problem was asked by Amazon.
# 
# Given a string, determine whether any permutation of it is a palindrome.
# 
# For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. 
# daily should return false, since there's no rearrangement that can form a palindrome.
from collections import Counter
def can_be_pal(word):
    c = Counter(word)
    odd_nums = 0
    
    for char, count in c.items():
        if count % 2 != 0:
            odd_nums += 1
    return odd_nums <= 1
    
def pal(word):
    odd_nums = 0
    chars = {}
    
    for x in word:
        if x not in chars:
            chars[x] = 1
        else:
            chars[x] += 1
    for x in chars:
        if chars[x] % 2 != 0:
            odd_nums += 1
    return odd_nums <= 1
            
            
    

print(pal('carrace'))