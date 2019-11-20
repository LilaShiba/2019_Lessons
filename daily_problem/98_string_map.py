# This problem was asked by Bloomberg.
# 
# Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
# 
# For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
# 
# Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.

def merge_sort(word):
    
    if len(word) > 1:
        
        n = len(word)
        mid = n//2
        l_half = word[:mid]
        r_half = word[mid:]
        
        merge_sort(l_half)
        merge_sort(r_half)
        
        ri,li,k = 0,0,0
        
        while ri < len(r_half) and li < len(l_half):
            if r_half[ri] > l_half[li]:
                word[k] = r_half[ri]
                ri+=1
            else:
                word[k] = l_half[li]
                li+=1
            k+=1
        
        while ri < len(r_half):
            word[k] = r_half[ri]
            ri+=1
            k+=1
        
        while li < len(l_half):
            word[k] = l_half[li]
            li+=1
            k+=1
            
    return word
    
    

def can_map(word1, word2):
    if len(word1) != len(word2):
        return False
    word1 = merge_sort(list(word1))
    word2 = merge_sort(list(word2))
    
    return word1 == word2
        
def slower_map(word1, word2):
    mapping = {}
    
    if len(word1) != len(word2):
        return False
    
    for char1, char2 in zip(word1, word2):
        if char1 not in mapping:
            mapping[char1] = char2
        elif mapping[char1] != char2:
            return False
            
        print(mapping)

if __name__ == '__main__':
    word1 = 'abcd'
    word2 = 'bcaa'
    print(can_map(word1, word2))
    print(slower_map(word1, word2))