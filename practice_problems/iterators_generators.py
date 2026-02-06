# Self-designed exercises from Chapter 17 of Fluent Python
import random
from typing import List

# Exercise 1: Build an iterable
class Iterable:
    # According to page 599 I need to implement the __iter__ method and return an iterator
    # It isn't enough to just implement an __iter__ method. We need to return an iterator that implements (__next__) 
    # because Python will first use iter() then next() and if we don't have an iterator then the next() call will fail
    
    def __init__(self, item_back: List):
        self.item = item_back
    
    def __iter__(self):
        # One of the lessons is that iterators come from iterables
        # It does not matter what type is passed into Iterable. It can be a collection or other types (e.g. files)
        return Iterator(self.item)

# Exercise 2: Build an iterator
class Iterator:
    def __init__(self, item):
        self.item = item
        # Iterators need some way to track the current item/next item but these objects can be different
        # E.g. in a graph this may be current_node or next_node
        self.index = 0

    def __next__(self):
        try:
            item = self.item[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return item

    def __iter__(self):
        # When we return self we return the object `Iterator`
        # We would like to return self because by returning the goal is to obtain an iterator
        # This is already an iterator so we just return it so it can be used
        return self

i = Iterable([1, 2, 3, 4, 5, 6])
# This testing method comes from: https://stackoverflow.com/questions/1952464/python-how-to-determine-if-an-object-is-iterable
try:
    # The `iter` checks for an __iter__ method on the instance of the class we made. If we comment it out we get a type error.
    test_iterator = iter(i)
except TypeError as te:
    print(f"test_iterator is not iterable")

# Exercise 3: Build one thing two different ways: Main thing is to contrast lazy v. eager evaluation using generators v. non-generator
# Plotting idea: Add the sizeof all these lists together in a plot to show memory and work done v. values consumed curve?
# Lists
# Step 1: Generate numbers
long_list = [1 if i % 4 else 0 for i in range(1, 100000)]
# Step 2: Transform them
transform_list = [random.randint(1, 10) * val if idx % 6 else val for idx, val in enumerate(long_list)]
# Step 3: Filter them
filtered_list = [i for i in transform_list if i % 2 == 0]
# Step 4: Slice the results (take the first k)
final_list = filtered_list[:100]

# Generators
# Just remember: The following builds several generator expressions that are linked together (each points to the previous)
# And in this setup generators only store and surface one value at a time. When we loop through one of these lists it
# resumes execution, computes next value, yields it (*review*)
# Step 1: Generate numbers
long_gen = (1 if i % 4 else 0 for i in range(1, 100000))
transform_gen = (random.randint(1, 10) * val if idx % 6 else val for idx, val in enumerate(long_gen))
filtered_gen = (i for i in transform_gen if i % 2 == 0)
# My workaround for generator objects not being slice-able
# We are not able to slice generators because they are iterables but not sequences because
# They do not implement __getitem__ or __len__ which are required
final_list = (val for idx, val in enumerate(filtered_gen) if idx < 100)

# Exercise 4: Contrast the sequence v. iterable protocol and build a custom type that is both a sequence and an iterable
class CustomType:
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        return Iterator(self.data)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.data[index]
        elif isinstance(index, slice):
            # Wrap this in CustomType so that the returned object is the same kind of object as the original
            return CustomType(self.data[index])
        else:
            raise TypeError(f"Type of index: {type(index)} is not supported")

    def __len__(self):
        return len(self.data)
    
    def __repr__(self):
        return f"CustomType({self.data})"

# All sequences are iterables so we can test if custom type is a sequence by trying to iterate through it
ct = CustomType([1, 2, 3, 4, 5, 6, 7])
# for i in ct: (This works!)
#     print(i)

# Let's also test that this is an iterable (we should get `True` CustomType implements __iter__ which returns an iterator)
try:
    ct_iterator = iter(ct)
    #print(True)
except TypeError as te:
        print("ct_iterator is not iterable")
