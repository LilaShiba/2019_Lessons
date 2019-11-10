# Given a list of words, return the shortest unique prefix of each word. 
# For example, given the list:
# 
# dog
# cat
# apple
# apricot
# fish
# 
# Return the list:
# 
# d
# c
# app
# apr
# f

class Node:
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.finished = False
        self.count = 0
        self.value = ''
        

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
                node.value = char
            node.count += 1
            node = node.children[char]
        node.finished = True
            
        
    def insert_string(self, lst):
        for word in lst:
            self.insert(word)
    
    def unique_prefix(self,word):
        node = self.root
        prefix = ''
        for char in word:
            if node.count == 1:
                return prefix
            #print(node.count)
            node = node.children[char]
            prefix += char
        return prefix
    
        


def prefix(words):
    trie = Trie()
    trie.insert_string(words)
    trie.show()
    
    return [trie.unique_prefix(char) for char in words]
    
print(prefix(['hello', 'world', 'heo']))
    
    