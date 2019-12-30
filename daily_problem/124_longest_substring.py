# This problem was asked by YouTube.
# 
# Write a program that computes the length of the 
# longest common subsequence of three given strings. 
# For example, given "epidemiologist", "refrigeration", 
# and "supercalifragilisticexpialodocious", it should 
# return 5, since the longest common subsequence is "eieio".

w1 = "supercalifragilisticexpialodocious"
w2 = "epidemiologist"
w3 = "refrigeration"
ans = "eietacocatio"



words = [w1,w2,w3]

def recursive(a,b):
    if not a or not b:
        return 0
    else:
        if a[0] == b[0]:
            return 1 + recursive(a[1:], b[1:])
        else:
            return max(recursive(a[1:],b), recursive(a, b[1:]))
        
print(recursive(w1,w2))

def dlcs(a,b):
    lengths = [[0 for x in range(len(b)+1)]for y in range(len(a)+1)]
    for i,x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                pass
    
    
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
    
#print(find_longest(words))