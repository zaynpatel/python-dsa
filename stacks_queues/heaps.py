# Problem 1 - Confirm a heap is actually a min heap.
#Design an algorithms that can check whether a heap (with array representation) is a valid min heap or not.
#Note: a valid min heap is when the parent node is smaller than the children - for all the nodes in the heap.
# implement from scratch with lots of pseudocode, woo!

# Completed on October 11, 2023 (1.5 hr)

"""
Confirming intuition for why some of these examples might fail:

The [5, 3, 8, 6, 4] fails because the rule of a min-heap is the parent is less than the children and 5 > 3.

The [1, 3, 5, 10, 9, 2, 4] works because 3 (parent) is less than 10 (child). 

Empty heaps return True because by definition they are valid min-heaps (and max-heaps I suppose). 

"""


def is_min_heap(heap):
    n = len(heap) # use this to determine where the last child node is so we don't evaluate leaf nodes since they don't have children and we don't care about their completeness
    # make sure to use integer division instead of extra parenthesis for order of operations since Python will run this out of order
    for i in range(0, (n - 1) // 2): # using this because I want the loop to iterate from the start of the indices to the point before out of bounds error
        sample_1 = 2 * i + 1
        sample_2 = 2 * i + 2
        # remember to compare the values in the list, not sample_1 and sample_2 which would be indices
        if heap[i] >= heap[sample_1] or heap[i] >= heap[sample_2]: # evaluate the opposite condition so we can return False. heap[i] is parent node and heap[sample_n] is child node     
            # if the parent >= child in either sample, return False which makes sense since this violates min_heap properties
            
            return False
    return True

# Problem 2 - Transform a max heap to a min heap.
# Completed on October 12, 2023 (3.5 hr)

"""
Confirming intuition for code definitions:

- self.heap is using the classes' built-in encapsulation methods to manipulate the heap across methods within the class so I don't have to pass it as an argument.

Notes:
- had to do a rewrite a few hours into the problem because there was an IndexError for one of the tested heaps. Realized that one thing I'd like to do in addition to storyboarding the 
code is, thinking of all exceptions to be handled and write code with these instead of patch after and rewrite. 
- Heapification has a runtime of O(n) because we don't have to traverse through the entire tree, we can look at the parent/child nodes but skip leaf nodes.
- Deleting an element has a runtime of O(log(n)) because we have to swap on the elements at the leaf node level


"""

class HeapTransformer:
    
    def __init__(self, heap):
        self.heap = heap

    def transform(self):
        n = len(self.heap)
        # scenario 2 in the fix_down function doesn't need an if statement, this loop will keep looping for parent_value is less than children
        for i in range(0, (n-1) // 2): # floor division rounds to nearest integer
            # want to check whether the parent >= children since this is what we need for converting max heap, where this is the case to a min heap where parent node is smaller than children
            if self.heap[i] >= self.heap[2 * i + 1] or self.heap[i] >= self.heap[2 * i + 2]:
                self.fix_down(i) # make sure we're referencing the index, not the value at i

    # there are three cases for swap operations
    # case 1: if the children are both less than the length of the heap it means there's more to traverse
    # case 2: if the left_child is less than the heap, it means the left child exists only and a swap needs to be made for that child only
    # case 3: if the right_child is less than the heap, it means the right child exists only and swap for this
    
    def fix_down(self, index):

        # confirm nesting 
        right_child = 2 * index + 2 
        left_child = 2 * index + 1
        parent_value = self.heap[index]
        # so when I initialize to none and then reinitialize with the value self.heap[left_child] what I'm doing is updating the value of None outside the block thus making it valid for later. 
        right_child_value = None # initialize these to none because when I reference them on line 77, they need to have values, otherwise there's a reference error
        left_child_value = None
        # use two independent if statements to check whether the values are in bounds before continuing with the rest of the flow
        if left_child < len(self.heap): 
            left_child_value = self.heap[left_child] # these variables are limited to scope defined
        if right_child < len(self.heap):
            right_child_value = self.heap[right_child]    
        
        # scenario 2 - parent value is greater than both, we need to pick one to swap with
        # shifted this before the other statement since it makes sense to check the most restructive condition first.
        # to do this, figure out which is larger and then make the swap

        if right_child_value is not None or left_child_value is not None: # will specifically check for None values instead of empty string, 0, any other value that could evaluate to False in Python
            if parent_value > right_child_value and parent_value > left_child_value:
                if right_child_value > left_child_value:
                    smaller_child = left_child # save their indices not the values since this will be swapped. intuitively I knew this but had to go back after error and fix since I had values swapping.
                else:
                    smaller_child = right_child
                        

                if left_child < len(self.heap) and right_child < len(self.heap):
                        self.heap[index], self.heap[smaller_child] = self.heap[smaller_child], self.heap[index]
                elif left_child < len(self.heap): # there still exists a left child
                    self.heap[index], self.heap[left_child] = self.heap[left_child], self.heap[index]
                elif right_child < len(self.heap):
                    self.heap[index], self.heap[right_child] = self.heap[right_child], self.heap[index]
                            
                # add a recursive call after the swap so the heap is maintained at the subtree. without this, [explain]
                self.fix_down(smaller_child)

            # check if the values are not None before evaluating
            # we can combine elif/if statements to check nested conditions
            elif right_child_value is not None and left_child_value is not None:
                # scenario 3 - the case where parent is larger than one of the nodes but smaller than the other
                if (parent_value > right_child_value and parent_value < left_child_value) or \
                    (parent_value < right_child_value and parent_value > left_child_value):
                    # Determine which child is smaller based on the scenario so we don't determine this unnecessarily
                    if right_child_value > left_child_value:
                        smaller_child = left_child
                    else:
                        smaller_child = right_child
                        # Make the swap if needed
                    if parent_value > self.heap[smaller_child]:
                        self.heap[index], self.heap[smaller_child] = self.heap[smaller_child], self.heap[index]
                        self.fix_down(smaller_child) # this recursive call confirms that we pass the smaller_child index through the `fix_down` function and ensures we maintain heap properties`

            

        

        