# # The game of Yahtzee is played by rolling five 6-sided dice, and scoring the results 
# in a number of ways. You are given a Yahtzee dice roll, represented as a sorted list of 
# 5 integers, each of which is between 1 and 6 inclusive. Your task is to find the maximum 
# possible score for this roll in the upper section of the Yahtzee score card. Here's what that means.
# 
# For the purpose of this challenge, the upper section of Yahtzee gives you six possible ways to score 
# a roll. 1 times the number of 1's in the roll, 2 times the number of 2's, 3 times the number of 3's, 
# and so on up to 6 times the number of 6's. For instance, consider the roll [2, 3, 5, 5, 6]. If you 
# scored this as 1's, the score would be 0, since there are no 1's in the roll. If you scored it as 
# 2's, the score would be 2, since there's one 2 in the roll. Scoring the roll in each of the six ways 
# gives you the six possible scores:
# 
# 0 2 3 0 10 6

def high_y(roll):
    table = {}
    for die in roll:
        if die not in table:
            table[die] = die
        else:
            table[die] += die
    return max(table.values())

def high_yy(roll):
    table = {}
    for x in roll:
        table.setdefault(x, 0)
        table[x] += x
    return max(table.values())
print(high_y([2, 3, 5, 5, 6]))



# This problem was asked by Google.
# 
# You are given a starting state start, a list of transition probabilities for a 
# Markov chain, and a number of steps num_steps. Run the Markov chain starting from start 
# for num_steps and compute the number of times we visited each state.
# 
# For example, given the starting state a, number of steps 5000, 
# and the following transition probabilities:

# [
#   ('a', 'a', 0.9),
#   ('a', 'b', 0.075),
#   ('a', 'c', 0.025),
#   ('b', 'a', 0.15),
#   ('b', 'b', 0.8),
#   ('b', 'c', 0.05),
#   ('c', 'a', 0.25),
#   ('c', 'b', 0.25),
#   ('c', 'c', 0.5)
# ]

# { 'a': 3012, 'b': 1656, 'c': 332 }