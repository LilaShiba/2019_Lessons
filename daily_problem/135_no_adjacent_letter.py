
str1 = 'aaabbcccccc'


def can_work(word):
    counts = {}
    for x in word:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    the_most = max(counts.values())
    return the_most <= (len(word) - the_most + 1), counts.get

# log(n)
def m_sort(word):
    if len(word) > 1:
        mid = len(word)//2
        r = word[mid:]
        l = word[:mid]
        
        m_sort(r)
        m_sort(l)
        
        i=j=k = 0
        while i < len(r) and j < len(l):
            if r[i] > l[j]:
                word[k] = l[j]
                j+=1
            else:
                word[k] = r[i]
                i+=1
            k+=1
        
        while i < len(r):
            word[k] = r[i]
            k+=1
            i+=1
        while j < len(l):
            word[k] = l[j]
            k+=1
            j+=1
    return ''.join(word)
# O(n)    
def can_be_done(word):   
    best = current = 0 
    same = word[0]
    for letter in word:
        if letter == same:
            current+=1
        else:
            if current > best:
                best = current
                char = letter
            same = letter
            current = 1
    
    if current > best:
        best = current
        char = letter
    print(best)

    return best <= len(word) - best+1, char
# O(n)
def solve(words):
    word = list(words)
    word = m_sort(word)
    proceed, letter = can_be_done(word)
    if proceed:
        arr_max = [x for x in word if x == letter]
        arr_les = [x for x in word if x != letter]
        print(arr_max, arr_les)
        ans = ""
        
        while arr_max:
            node_m = arr_max.pop()
            ans+=node_m
            if arr_les:
                node_l = arr_les.pop()
                ans+=node_l
        return ans
        
        

print(solve(str1))