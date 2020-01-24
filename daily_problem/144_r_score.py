# This problem was asked by Palantir.
# 
# In academia, the h-index is a metric used to 
# calculate the impact of a researcher's papers. 
# It is calculated as follows:
# 
# A researcher has index h if at least h of her 
# N papers have h citations each. If there are 
# multiple h satisfying this formula, the maximum is chosen.
# 
# For example, suppose N = 5, 
# and the respective citations of each paper are [4, 3, 0, 1, 5].
#  Then the h-index would be 3, since the researcher has 3 papers 
#  with at least 3 citations.
import random
papers = [random.randint(0,10) for x in range(10)]
p2 = [5,2,1,0,6]
# 6,5,4,2,1,0
def msort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        r = arr[mid:]
        l = arr[:mid]
        
        msort(r)
        msort(l)
        
        i=j=k=0
        
        while i < len(r) and j < len(l):
            if r[i] > l[j]:
                arr[k] = r[i]
                i+=1
            else:
                arr[k] = l[j]
                j+=1
            k+=1
        
        while i < len(r):
            arr[k] = r[i]
            i+=1
            k+=1
        
        while j < len(l):
            arr[k] = l[j]
            j+=1
            k+=1
        return arr

def the_most(h, papers):
    if len(papers[:h])+1 >= papers[h]:
        return True
    return False

    
def h_score(papers):
    spapers = msort(papers)
    h = 1
    for idx, cites in enumerate(spapers):
        if cites >= h:
            h+=1
        else:
            return h-1
    return h-1

print(papers)
print(h_score(papers))
