
# This problem was asked by IBM.
# 
# Given an integer, find the next permutation 
# of it in absolute order. For example, given 48975, 
# the next permutation would be 49578

def next_num(num):
    num = [int(x) for x in str(num)] 
    n = len(num)
    tail_start = n - 1
    
    # find first left less than right going backwards
    while tail_start >= 0 and num[tail_start-1] > num[tail_start]:
        tail_start -= 1
    # if in descending order, can't be done
    if tail_start == 0:
        return None
    
    # swap smallest digit in tail that is larger than the digit needed to swap with
    swap = tail_start
    while swap < n and num[tail_start-1] < num[swap]:
        swap += 1
    swap -= 1
    
    #swap
    num[tail_start-1], num[swap] = num[swap], num[tail_start-1]
    
    # reverse tail elements
    start,end = tail_start, len(num)-1
    while start < end:
        num[start], num[end] = num[end], num[start]
        start+=1
        end -= 1
    
    return num
    
    
    
    
            

t1 = 48975
a1 = 49578

print(next_num(t1))