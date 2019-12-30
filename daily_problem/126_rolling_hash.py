# This problem was asked by Microsoft.
# 
# Given a string and a pattern, find the starting indices 
# of all occurrences of the pattern in the string. For example, 
# given the string "abracadabra" and the pattern "abr", 
# you should return [0, 7].


txt = "abracadabr"
pattern = "abr"
ans = [0,7]

def find_pattern_matches1(txt, pattern):
    matches = []
    n = len(pattern)
    for x in range(len(txt)-n+1):
        if txt[x:x+n] == pattern:
            matches.append(x)
    return matches
    
def find_match(txt, pattern):
    matches = []
    n = len(pattern)
    
    for x in range(len(txt)-n+1):
        if txt[x:x+n] == pattern:
            matches.append(x)
    return matches

def value(letter):
    return ord(letter) - 96

def roll_hash(prev, start, new):
    return prev-value(start)+value(new)
    
def rolling_hash(txt, pattern):
    matches = []
    hash = {}
    n = len(pattern)
    pattern_value = 0
    hash_val = 0
    # get pattern value
    for char in pattern:
        pattern_value += value(char)
    # get first n length of txt value
    for char in txt[:n]:
        hash_val += value(char)    
    # check first instance
    if hash_val == pattern_value:
        matches.append(0)
    # roll hash
    for i in range(len(txt)-n):
        hash_val = roll_hash(hash_val, txt[i], txt[i+n])
        if hash_val == pattern_value:
            if txt[i+1:i+n+1] == pattern:
                matches.append(i+1)
    print(matches)
    
    
print(find_pattern_matches1(txt,pattern))
print(find_match(txt, pattern))
print(rolling_hash(txt,pattern))