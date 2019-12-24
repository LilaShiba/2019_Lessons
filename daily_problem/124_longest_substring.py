# This problem was asked by YouTube.
# 
# Write a program that computes the length of the 
# longest common subsequence of three given strings. 
# For example, given "epidemiologist", "refrigeration", 
# and "supercalifragilisticexpialodocious", it should 
# return 5, since the longest common subsequence is "eieio".

w1 = "tacocat"
w2 = "refrigerationtacocatrefri"
w3 = "supercalifragilisticexpialodocious"
ans = "eietacocatio"

words = [w1,w2,w3]
def find_longest(words):
    w1,w2,w3 = words
    
    def kadens(word):
        highest = ''
        n = len(word)
        for start in range(0, n):
            for end in range(start, n):
                substr = word[start:end]
                if is_palindrome(substr):
                    if len(substr) > len(highest):
                        highest = substr
                
        return highest    
    def is_palindrome(word):
        return word == word[::-1]
    
    
    ans = kadens(w2)
    print(ans)
    
print(find_longest(words))