# This problem was asked by Facebook.
# 
# Boggle is a game played on a 4 x 4 grid of letters. 
# The goal is to find as many words as possible that 
# can be formed by a sequence of adjacent letters in 
# the grid, using each cell at most once. Given a game 
# board and a dictionary of valid words, implement 
# a Boggle solver.

grid = [["a", "b", "c", "d"],
        ["x", "a", "y", "z"],
        ["t", "z", "r", "r"],
        ["s", "q", "q", "q"]]

dictionary = ['bat', 'car', 'cat']

def boggle(grid, dictionary):
    row = len(grid)
    col = len(grid[0])
    
    def make_trie(words):
        root = {}
        
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict['#'] = "#"
        return root
    

    def get_neighbors(x,y): 
        neighbors = (
            (x+1, y), (x-1, y), (x, y-1), (x, y+1), (x+1, y+1),
            (x-1,y-1), (x+1, y-1), (x-1, y+1)
        )
        
        real_neighbors = ((cx,cy) for (cx,cy) in neighbors if 0<= cx < 3 and 0<= cy < 3)
        return real_neighbors          


    def bfs(location,current_trie,letter):
        stack = [location]
        visited = []
        word = [letter]
        
        while stack:
            node = stack.pop(0)
            if node not in visited:
                visited.append(node)
                x,y = node
                
                for cx,cy in get_neighbors(x,y):
                    next_letter = grid[cx][cy]
                    print(next_letter)

                    if next_letter in current_trie:
                        word.append(next_letter)
                        print(word)
                        next_trie = current_trie[next_letter]
                        stack.append((cx,cy))
                        current_trie = next_trie
                        if '#' in current_trie:
                            return word
        return None
        
    trie = make_trie(dictionary)
    print(trie)
    ans = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            letter = grid[row][col]
            if letter in trie:
                word = bfs((row,col),trie[letter], letter)
                print(word)
                if word != None:
                    print('wow')
                    ans.append(word)     
    return [''.join(x) for x in ans]               
                    



def m_trie(words):
    trie = {}
    
    for word in words:
        current = trie
        for letter in word:
            current = current.setdefault(letter, {})
        current["#"] = '#'
    return trie
    
        


def all_perms(arr):
    ans = []
    if len(arr) == 1:
        return [arr]
    
    for item in range(len(arr)):
        # current iterative item
        current = arr[item]
        # all items save for current item
        temp = arr[:item] + arr[item+1:]
        
        for perm in all_perms(temp):
            print(perm)
            ans.append(perm + [current])
        
    return ans
arr = [1,2,3]    
#print(make_trie(dictionary))
#print(m_trie(dictionary))
print(boggle(grid, dictionary))