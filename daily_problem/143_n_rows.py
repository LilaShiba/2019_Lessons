# This problem was asked by Spotify.
# 
# There are N couples sitting in a row of length 2 * N. 
# They are currently ordered randomly, but would like to 
# rearrange themselves so that each couple's partners 
# can sit side by side.
# 
# What is the minimum number of swaps necessary for this to happen?

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
r = [3, 2, 0, 1]
print(min_swaps(r))