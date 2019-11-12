# This problem was asked by Airbnb.
#
# Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.
#
# For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].


def is_palindrom(word1, word2):
    word = word1 + word2
    print(word, word[::-1])
    return word == word[::-1]

def unique_palindroms(lst):
    ans = []
    for x in range(len(lst)):
        for y in range(len(lst)):
            if y != x and is_palindrom(lst[x], lst[y]):
                ans.append((x,y))
    return ans



arr = ["code", "edoc", "da", "d"]
print(unique_palindroms(arr))
