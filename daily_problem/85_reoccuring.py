# This problem was asked by Google.
# 
# Given a string, return the first recurring character in it, or null if there is no recurring character.
# 
# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

def navie(word):
    checky = ''
    for x in word:
        if x in checky:
            return x
        else:
            checky+=x
    return False
    
print(navie('acbbac'))

# We can improve the space complexity by using bitwise operators to set the bits of characters already seen in the string:

def first_recurring(str):
    checker = 0
    for c in str:
        val = ord(c) - ord('a')
        if (checker & (1 << val)) > 0:
            return c
        checker |= (1 << val)
    return None
    
print(first_recurring('acbbac'))
