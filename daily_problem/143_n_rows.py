# This problem was asked by Spotify.
# 
# There are N couples sitting in a row of length 2 * N. 
# They are currently ordered randomly, but would like to 
# rearrange themselves so that each couple's partners 
# can sit side by side.
# 
# What is the minimum number of swaps necessary for this to happen?

import random
def min_swaps(row):
    # get position of each person
    peoplePos = {idx:i for i,idx in enumerate(row)}
    # function to get partner. If odd go left to get partner 
    # if even of right to get partner
    getPartner = lambda x: x-1 if x%2!=0 else x+1
    
    # keep track of swaps 
    idx = ans = 0
    # begin swapping
    while idx < len(row):
        current = row[idx]
        partner = getPartner(current)
        partner_idx = peoplePos[partner]
        
        # get location of swap (left or right)
        swap_pos = partner_idx - 1 if partner_idx % 2 != 0 else partner_idx+1
        location_of_swap = row[swap_pos]
        # if needs to make swap
        if swap_pos != idx:
            ans += 1
            # make swap
            row[idx], row[swap_pos] = row[swap_pos], row[idx]
            # update dict
            peoplePos[current], peoplePos[location_of_swap] = peoplePos[location_of_swap], peoplePos[current]
        else:
            idx+=1
    return ans


def couple_swap(row: list) -> int:
    person_location = {idx:person for person, idx in enumerate(row)}
    get_partner = lambda x: x+1 if x%2 == 0 else x-1
    
    swaps = 0
    idx = 0
    
    while idx < len(row):
        # get current person
        current = row[idx]
        # get their partner num
        partner = get_partner(current)
        # get partner location via index
        partner_idx = person_location[partner]
        # get location of swap
        swap_pos = partner_idx -1 if partner_idx % 2 != 0 else partner_idx + 1
        location_of_swap = row[swap_pos]
        # check to see if swap is needed
        if swap_pos != idx:
            # if need to swap, do so
            row[idx], row[swap_pos] = row[swap_pos], row[idx]
            # increment swaps count
            swaps += 1
            # update dict 
            person_location[current], person_location[location_of_swap] = person_location[location_of_swap], person_location[current]
        else:
            #increment loop 
            idx +=1
    # return swap count
    return swaps


def swap_couples(row: list) -> int:
    locations = {value:idx for idx, value in enumerate(row)}
    get_partner = lambda x: x-1 if x%2 != 0 else x+1
    
    idx=ans=0
    n = len(row)
    while idx < n:
        # get current value 
        current = row[idx]
        # get partner value 
        pv = get_partner(current)
        # get partner idx 
        pl = locations[pv]
        # get swap location 
        sl = pl -1 if pl % 2 != 0 else pl + 1
        # get value location of swap 
        sl_v = row[sl]
        # check if swap is needed 
        if idx != sl:
            ans +=1
            # make swap 
            row[idx], row[sl] = row[sl], row[idx]
            # update dict 
            locations[current], locations[sl_v] = locations[sl_v], locations[current]
        else:
            idx+=1
    return ans
        
r = [3,5,1,6,7,8,2,9,0,4]
print(min_swaps(r)) 
r = [3,5,1,6,7,8,2,9,0,4]
print(couple_swap(r)) 
print(r)
r = [3,5,1,6,7,8,2,9,0,4]
print(r)

print(swap_couples(r))      