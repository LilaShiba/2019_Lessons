# This problem was asked by Facebook.
# 
# Given a number in Roman numeral format, convert it to decimal.
# 
# The values of Roman numerals are as follows:
roman_numerals = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

numerals_roman = {
    1000: 'M',
    500:  'D',
    100:  'C',
    50:   'L',
    10:   'X',
    5:    'V',
    1:    'I'
}

# In addition, note that the Roman numeral system 
# uses subtractive notation for numbers such as IV and XL.
# 
# For the input XIV, for instance, you should return 14.

q1 = "XIV"
a1 = 14
q2 = "MCCXIV"
a2 = 1214

def num_to_roman(num):
    pass
    
def make_roman1(num):
    total = 0
    for i in range(len(num)-1):
        if roman_numerals[num[i]] >= roman_numerals[num[i+1]]:
            total += roman_numerals[num[i]]
        else:
            total -= roman_numerals[num[i]]
    total += roman_numerals[num[-1]]
    return total
    
def make_roman(num):
    temp = []
    for x in range(len(num)-1):
        # get current num and next num
        current_num = roman_numerals[num[x]]
        next_num = roman_numerals[num[x+1]]
        # if subtractive property mark with 1
        if current_num < next_num:
            temp.append((current_num, 1))
        else:
            temp.append((current_num, 0))
    # add last num        
    last_num = roman_numerals[num[-1]]
    temp.append((last_num, -1))
    
    ans = 0
    # if needing to subtract add placeholder
    hold_sub = False
    # amount to subtract by 
    sub_temp = 0
    
    for num, sub in temp:
        # if you need subtractive property 
        if sub == 1:
            # set place holder
            hold_sub = True
            # hold numer to subtract by
            sub_temp = num 
        # if previous number rasied subtractive flag
        elif hold_sub == True:
            # subtract 
            new_num = num - sub_temp
            # add to number
            ans += new_num 
            # reset subtractive number
            sub_temp = 0
            # reset flag
            hold_sub = False
        else:
            ans += num
    return ans
        

print(make_roman(q2))
print(make_roman1(q2))