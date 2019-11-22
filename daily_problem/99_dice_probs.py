# This problem was asked by Two Sigma.
# 
# Alice wants to join her school's Probability Student Club. Membership dues are 
# computed via one of two simple probabilistic games.
# 
# The first game: roll a die repeatedly. Stop rolling once you get a five followed 
# by a six. Your number of rolls is the amount you pay, in dollars.
# 
# The second game: same, except that the stopping condition is a five followed by a five.
# 
# Which of the two games should Alice elect to play? Does it even matter? Write a program 
# to simulate the two games and calculate their expected value.

import random
def game_one():
    rolls = 0
    simulations = 0
    five_six = False
    
    while five_six is False:
        rolls += 2
        simulations += 1
        roll1 = random.randint(1,7)
        roll2 = random.randint(1,7)
        if roll1 == 5 and roll2 == 6:
            return rolls

def game_one_better(simulations=100000):
    rolls = 0
    money = 0
    success = 0
    for x in range(simulations):
        roll1 = random.randint(1,7)
        roll2 = random.randint(1,7)
        if roll1 == 5 and roll2 == 6:
            success += 1
            rolls = True
        if rolls == False:
            money += 1
    return 100*(success/simulations), money

def game_two(seq, simulations=100000):
    rolls = 0
    success = 0
    for x in range(simulations):
        roll1 = random.randint(1,7)
        roll2 = random.randint(1,7)
        if roll1 == seq[0] and roll2 == seq[1]:
            success += 1
    return 100*(success/simulations)

                
def probs(roll1, roll2):
    pass
    
#print(game_one_better())

    
print(seq1, seq2)