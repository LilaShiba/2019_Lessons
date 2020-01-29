def min_change(coins, n):
    cache = [0 for _ in range(n+1)]
    
    for coin in coins:
        if coin < len(cache):
            cache[coin] = 1
    print(cache)
    
    for i in range(1, n+1):
        cache[i] = min(1+cache[i-coin] for coin in coins if i-coin >= 0)
    
    return cache[n]

print(min_change([1,2,5,10,25], 15))
