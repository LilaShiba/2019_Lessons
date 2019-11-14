# Given a start word, an end word, and a dictionary of valid words, 
# find the shortest transformation sequence from start to end such 
# that only one letter is changed at each step of the sequence, 
# and each transformed word exists in the dictionary. If there is no 
# possible transformation, return null. Each word in the dictionary 
# have the same length as start and end and is lowercase.


start = "dog"
end = "cat"  
dictionary = ["dot", "dop", "dat", "cat"]
ans = ["dog", "dot", "dat", "cat"]
import string
import queue 
# make graph
def ladder_length(start_word, end_word, word_list):
    queue = [start_word]
    graph = {}
    seen = []
    while queue:
        word = queue.pop(0)
        graph[word] = []
        # end case
        if word == end_word:
            return graph
        # check permutations
        for idx in range(len(word)):
            for char in string.ascii_lowercase:
                next_word = word[:idx] + char + word[idx+1:]
                if next_word in word_list and next_word not in seen:
                    queue.append(next_word)
                    graph[word].append(next_word)
                    seen.append(next_word)
    return 'nope'
                    
# do bfs
def word_bfs(start_word, end_word, graph):
    queue = [[start_word]]
    visited = []
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        print(node)
        
        if node == end_word:
            return path
        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    
    return path
                    
    
ans2 = ladder_length(start,end,dictionary)
print(ans2)
ans3 = word_bfs(start, end, ans2)
print(ans == ans3)  
        