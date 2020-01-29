def fib1(n):
    # if n <= 1:
    #     return n 
    # else:
    a, b = 0, 1
    for _ in range(n):
        a,b = b, a+b 
    return a
        

def dp_fib(n):
    memo = [0,1]
    for i in range(2, n+1):
        m = memo[i-1] + memo[i-2]
        memo.append(m)
    #print(memo)
    return memo[n]

print(fib1(150))
print(dp_fib(150))