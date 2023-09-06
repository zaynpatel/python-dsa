# I want to test if this is correct for a stack data structure

"""
There are a few things I'm learning about the implementation below:

- First, when I write s.pop() the initial time, it removes the last item in the list. I can add it as many times as I want until it reaches a condition I want. 

For example, if I want .pop() to continue until are lists are empty, I can do this. Or, until all lists have at least two elements, I can do this too. 

- Second, .pop() method doesn't work on integers and in order to have a stack I'd need a 2D list structure so there's something to hold all the contents and something that can be removed and appended. 

- Third, when practice problems talk about adding new memory to solve the problem, one way I can do this is by adding an empty list that appends items from the first list to it. I did this in trying to handle an empty list. 

stacks = [[1, 4, 5, 7], [4, 5], [6, 78, 99], [10, 24, 33]]
new_stacks = [] -> this is the new list instantiation I'm talking about
for s in stacks:
    if s:
        s.pop()
        new_stacks.append(s) -> this is the new list appending I'm talking about
stacks = new_stacks
print(stacks)

"""

stacks = [[1, 4, 5, 7], [4, 5], [6, 78, 99], [10, 24, 33]]
for s in stacks:
    s.pop()
    s.pop()
    s.pop()

print(stacks)

# Implementing queue from scratch

class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return self.queue == []
    
    # needed help on this one
    def enqueue(self, data):
        self.queue.append(data)
    
    # always going to return the first item of the array
    # this has an O(n) running time because we have to move the items to the list
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)
    
# Coding exercise: Max in a stack problem overview
"""

The s > max_stack[-1] works because up until this code block there's nothing in max_stack. 
We can write this because we've included an or statment so s can be compared to the empty list and not throw an error. 
If there is an empty list, s will be included. Then, we'll compare the item again and we'll append. 
All of these appendings happen at the end of the list which is why if we're asking for just an int, returning the [-1] of the max_stack list makes sense. 

"""
def find_max_stack(stack):
    # initialize two lists so I can store the same elements in different order and return the max_item
    main_stack = []
    max_stack = []

    # loop through the stack
    for s in stack:
        # add each element to the main_stack list
        main_stack.append(s)
        # check to make sure the max_stack is not empty and compare the two items (current and last item in max_stack), then append it to max_stack
        if not max_stack or s > max_stack[-1]:
            max_stack.append(s)
    return max_stack[-1]

# Coding exercise: Queue with stack problem
# used for enqueue (insert an element into queue)

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, data):
        return self.stack1.append(data)
    
    def dequeue(self):
        # just need to have stack1 with elements to do the dequeue since this is where we're removing elements from to place them in stack2
        if not self.stack2:
            # check if stack1 is empty, if they are both empty, then the queue is empty and there's no reason to run
            if not self.stack1:
                return "Queue is empty"
            # in Python it's not a good idea to have a for loop when I'm modifying any list so I'm using a while loop 
            while self.stack1:
                # s is the element, iterating through stack1
                # because we're popping from stack1 and immediately adding to stack2, I can chain the pop and append
                # chaining will execute the pop first, append second
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            return "Queue is empty"
        
        # this will work via FIFO because of how we popped elements above
        return self.stack2.pop()




            




        