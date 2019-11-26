# This problem was asked by Google.
# 
# Given a string, split it into as few strings as possible such that each string is a palindrome.
# 
# For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].
# 
# Given the input string abc, return ["a", "b", "c"].

words = 'racecarannakayak'
ans = ["racecar", "anna", "kayak"]
words2 = 'step on no pets'
def is_palindrome(word):
    if len(word) > 0:
        return word == word[::-1]
    
def all_pals(words):
    ans = []
    for y in range(len(words)):
        for x in range(y, len(words)+1):
            if is_palindrome(words[y:x]):
                ans.append(words[y:x])
    return ans

def pals(words, combos):
    print(words)
    ans = []
    combos = sorted(combos, key=len, reverse=True)
    for x in combos:
        if x in words:
            ans.append(x)
            words = words.replace(x,'')
            print(words)
    return ans        
    
    
    
all_words = all_pals(words2)
print(pals(words2, all_words))
        