# You're given a string consisting solely of (, ), and *.  
# * can represent either a (, ), or an empty string. 
# Determine whether the parentheses are balanced.
# 
# For example, (()* and (*) are balanced. )*( is not balanced.

def is_balanced(word):
    par = either = 0
    # keep track
    for char in word:
        if char == "(":
            par += 1
        elif char == ")":
            par -= 1
        else:
            either += 1
    # case of balanced () and even **
    if par == 0 and either % 2 == 0:
        return True
    return par - either == 0
    
    

if __name__ == "__main__":
    balanced = "(()*"
    not_balance = ")*("
    print(is_balanced(balanced))
    print(is_balanced(not_balance))