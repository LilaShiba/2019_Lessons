def fib1(n):
    if n <= 1:
        return n 
    else:
        a, b = 0, 1
        for _ in range(n):
            a,b = b, a+b 
        return a
        
print(fib1(15))