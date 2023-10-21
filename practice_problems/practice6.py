# Problem - Two Sum on Leet Code
# Date: October 21, 2023 (90)
def two_sum(nums, target):
    d = {}  # initialize a dictionary for lookups

    # for loop to iterate through the list
    for i, num in enumerate(nums):
        complement = target - num
        if complement in d:
            return [d[complement], i]
        
        d[num] = i

# Problem - Non repeating strings
# Date: October 21, 2023
def char_string(string):
    my_dict = {}
    for input in string:
        my_dict[input] = my_dict.get(input, 0) + 1
    
    # iterate through the string because we want to ensure there's no order
    for input in string: # had to swap this with previous for loop which used .items() because .items() shows in the order items were inserted
        if my_dict[input] == 1: 
            return input