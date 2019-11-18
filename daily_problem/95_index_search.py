 # This problem was asked by Dropbox.

# Given a string s and a list of words words, where each word 
# is the same length, find all starting indices of substrings 
# in s that is a concatenation of every word in words exactly once.
 
s = "dogcatcatcodecatdog" 
words = ["cat", "dog"] 
 # return [0, 13]
 
def find_us(s, words):
    word1 = words[0]
    len_1 = len(word1)
    word2 = words[1]
    len_2 = len(word2)
    
    ans = []
    n = len(s)
    
    for char in range(n-len_1):
        if s[char:char+len_1+len_2] == word1+word2:
            found = (char, s[char:char+len_1+len_2])
            ans.append(found)
            break
    
            
    for idx in range(n-len_2):
        if s[idx:idx+len_2+len_1] == word2+word1:
            found = (idx, s[idx:idx+len_2+len_1])
            ans.append(found)
            break
        
    return ans

print(find_us(s,words))