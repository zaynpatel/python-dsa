# 1 - Reversing an array in-place exercise (using built - in methods)
def reversing(nums):
    # the reverse method is a Python in-place operation which means it modifies the item "in-place" but does not create a new one (new list in this case)
    nums.reverse(nums)
    return nums

# 1 - Using algorithms (from chatgpt, although I have intuition)
def reversing(nums):

    # initialize two pointers
    left = 0
    right = len(nums) - 1

    while left < right:
        # Swap the elements at the pointers
        nums[left], nums[right] = nums[right], nums[left]

        # Move the pointers closer to the middle
        left += 1
        right -= 1

    return nums

#2 - Palindrome exercise (using string slicing)
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else: 
        return False

# 2 Using algorithms (from chatgpt, although I have intuition)
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

# 3 Using algorithms (from chatgpt)
def reverse_integer(n):
    result = 0
    while n != 0:
        result = result * 10 + n % 10
        n = n // 10
    return result

# Anagram creation (chatgpt)
def are_anagrams(s1, s2):
    # if they aren't consistent length, they can't be anagrams
    if len(s1) != len(s2):
        return False
    
    # create two lists with 26 0's
    char_count1 = [0] * 26
    char_count2 = [0] * 26

    for char in s1:
        # calculates the difference between the ascii value of the character
        # and the ascii value of a so it knows where the value in the alphabet is
        # as a result, it increments this count in the list of 26 0's
        char_count1[ord(char) - ord('a')] += 1

    for char in s2:
        char_count2[ord(char) - ord('a')] += 1

    return char_count1 == char_count2
