# This problem was asked by Facebook.
# 
# Given a string of parentheses, find the balanced string that can be 
# produced from it using the minimum number of insertions and deletions. 
# If there are multiple solutions, return any of them.
# 
# For example, given "(()", you could return "(())". 
# Given "))()(", you could return "()()()()".

t1 = "(()"
a1 = "(())"

t2 = "))()("
a2 = "()()()()"

def balance(word):
    ans = []
    open_count = 0
    
    for x in word:
        if x == '(':
            open_count += 1
            ans.append(x)
        
        else:
            if not open_count:
                ans += '('
            else:
                open_count -= 1
            ans.append(x)
    
    while open_count:
        open_count -= 1
        ans.append(')')
        
    
    return ''.join(ans)

print(balance(t2))