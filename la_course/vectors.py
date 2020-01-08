import numpy as np

def sum_of_squares(a):
    return sum([x*x for x in a])
    
def vector_size(a):
    return np.sqrt(sum([x*x for x in a]))

# (a[0] * b[0]) + (a[1] * b[1]) + ...nth
def dot_product(a,b):
    dp = 0
    for x in range(len(a)):
        dp += (a[x]*b[x])
    return dp 

# a onto b
# a.b/|b|
def scalar_projection(a,b):
    return dot_product(a,b)/vector_size(b)

# a onto b
#  a.b/|b| * b/|b|
def vector_projection(a,b):
    modb = vector_size(b)
    aDotb = dot_product(a,b)
    first_half = (aDotb/modb)
    second_half = [first_half*x for x in b]
    return [x/modb for x in second_half]

# r.x / sum_of_squares(x)
def basis_change(r, vectors):
    ans = []
    for x in vectors:
        top = dot_product(r,x)
        bottom = sum_of_squares(x)
        ans.append(top/bottom)
    return ans
    
    
s = [3,2,4]
r = [-1,2-3]
#print(vector_size(r))
#print(dot_product(r,s))
#print(scalar_projection(s,r))
print(vector_projection(s,r))
v = [-4,-3,8]
b1 = [1,2,3,]
b2 = [-2,1,0]
b3 = [-3,-6,5]

s1 = [3,2,4]
v = [-1,2,-3]
print(basis_change(s1, [v]))
        