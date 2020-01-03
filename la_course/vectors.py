import numpy as np

def vector_size(a):
    return np.sqrt(sum([x*x for x in a]))

def dot_product(a,b):
    dp = 0
    for x in range(len(a)):
        dp += (a[x]*b[x])
    return dp 

# a onto b
def scalar_projection(a,b):
    return dot_product(a,b)/vector_size(b)

# a onto b
def vector_projection(a,b):
    modb = vector_size(b)
    aDotb = dot_product(a,b)
    first_half = (aDotb/modb)
    second_half = [first_half*x for x in b]
    return [x/modb for x in second_half]
    
    

s = [10,5,-6]
r = [3,-4,0]
#print(vector_size(r))
#print(dot_product(r,s))
#print(scalar_projection(s,r))
print(vector_projection(s,r))
        