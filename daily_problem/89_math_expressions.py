# The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.
# 
# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, 
# 
# since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

# https://en.wikipedia.org/wiki/Polish_notation


def form_expression(lst):
    PLUS = '+'
    MINUS = '-'
    TIMES = '*'
    DIVDE = '/'
    OPERANDS = [PLUS, MINUS, TIMES, DIVDE]
    stack = []
    for char in lst:
        if char in OPERANDS:
            expression1, expression2 = stack.pop(), stack.pop()
            if char == PLUS:
                stack.append(expression1 + expression2)
            elif char == MINUS:
                stack.append(expression1 - expression2)
            elif char == TIMES:
                stack.append(expression1 * expression2)
            else:
                stack.append(expression1 / expression2)
        else:
            stack.append(char)
    return stack


print(form_expression( [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']))            