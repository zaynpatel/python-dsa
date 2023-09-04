# 1* (python methods)
def replace_vowels(string, character):
    vowels = 'aeiou'
    for vowel in vowels:
        string = string.replace(vowel, character)
    return string 

# 2 (classes)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"

"""
Recall: to instantiate the class, we'll write:

bob = Person("Bob", 30)
in other words: var = className(func_param1, func_param2)
"""

# 3 (nested loops)
def flatten_list(nested_list):
    new_list = []
    for sublist in nested_list:
        for elements in sublist:
            new_list.append(elements)
    return new_list 

# 4* (classes)
class Matrix: 
    def add_matrices(self, A, B):
        # this checks for homogeniety between the rows and columns
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Both matrices must have the same dimensions")
        # initialize result as a 2D list with 0's. the values will change when you call the function
        result = [[0] * len(A[0]) for _ in range(len(A))]
        # to solve the matrix multiplication problem I need nested loops
        for i in range(len(A)):
            for j in range(len(A[0])):
                result[i][j] = A[i][j] + B[i][j]
        return result
    # do I need to rewrite this for a (+/-) change? There's no change of time compute b/c it's not a loop, the programmer calls this function with .subtract_matrices after they instantiate the class
    def subtract_matrices(self, A, B):
        # this checks for homogeniety between the rows and columns
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Both matrices must have the same dimensions")
        # initialize result as a 2D list with 0's. the values will change when you call the function
        result = [[0] * len(A[0]) for _ in range(len(A))]
        # to solve the matrix multiplication problem I need nested loops
        for i in range(len(A)):
            for j in range(len(A[0])):
                result[i][j] = A[i][j] - B[i][j]
        return result
    def multiply_matrices(self, A, B):
        # Check that the number of columns in A is equal to the number of rows in B
        if len(A[0]) != len(B):
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix")

        # Initialize result as a 2D list with 0's
        result = [[0] * len(B[0]) for _ in range(len(A))]

        # Iterate over rows of A
        for i in range(len(A)):
            # Iterate over columns of B
            for j in range(len(B[0])):
                # Iterate over columns of A/rows of B
                for k in range(len(A[0])):
                    result[i][j] += A[i][k] * B[k][j]
        return result

# working with stacks
s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')
print(s)

while s:
    print(s.pop())
if not s:
    raise ValueError("Stack is empty - test. ")

# this works but unoptimal b/c takes too long
def duplicate_number(array_nums):
    character_count = {}
    for word in array_nums:
        if word in character_count:
            character_count[word] += 1
        else: 
            character_count[word] = 1
    
    max_word_dict = dict(max(character_count.items(), key = lambda item: item[1]))
    return max_word_dict

def findDuplicate(nums):
    # the technique defined here is tortoise and the haire where one pointer follows the other
    # because of the algorithm, the two variables are initialized at the 0th index of the numbered list
    tortoise = nums[0]
    hare = nums[0]

    # want to start an infinite loop b/c 
    while True:
        # nums[tortoise] notation simply indexes the list and moves one step forward based on the current position
        tortoise = nums[tortoise]
        # move the hare two steps up (this is where the variant of floyd's cycle detection algo comes in. use two pointers with one 2x the speed of the other.)
        # this syntax is equivalent to saying move the hare twice. 
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    hare = nums[0]
    while tortoise != hare:
        hare = nums[hare]
        tortoise = nums[tortoise]
    return hare 