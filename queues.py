from typing import List, Tuple

class QueueException(BaseException):
    pass

# First just implement a basic queue
class Queue:
    def __init__(self, size_of_queue: int):
        self.queue: List = []
        self.size_of_queue = size_of_queue

    def enqueue(self, value, limit: int):
        if len(self.queue) <= limit:
            self.queue.append(value)
        else:
            raise QueueException(f"Size of queue: {self.size_of_queue} is larger than limit: {limit}")
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
        
    def is_empty(self):
        if not self.queue:
            return True
        else:
            return False
    
    def is_full(self, limit: int):
        if len(self.queue) > limit:
            return 1
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

# Then implement a priority queue (two ways)
class MaxPriorityQueueMethod1:
    """Implements `insert` in O(1) and `extract_max` in O(n)"""
    def __init__(self):
        self.priority_queue = []
    
    def insert(self, value: Tuple):
        return self.priority_queue.append(value)
    
    def extract_max(self):
        if not self.priority_queue:
            return "There are no elements"
        highest = self.priority_queue[0]
        for elt in self.priority_queue:
            if elt[1] > highest[1]:
                highest = elt
        # Update the priority queue to remove all elements that are the highest
        # This is better than .remove() since that only remove the first occurence of something
        self.priority_queue = [elts for elts in self.priority_queue if elts != highest]
        assert highest not in self.priority_queue
        return highest

class MaxPriorityQueueMethod2:
    """Implements `insert` in O(n) and `extract_max` in O(1)"""
    def __init__(self):
        self.priority_queue = []
    
    def insert(self, value: Tuple):
        if len(self.priority_queue) == 0:
            return self.priority_queue.append(value)
        for idx, elt in enumerate(self.priority_queue):  # I think this is the problem -- it keeps looping through the existing queue but does not bring in new elements
            if value[1] < elt[1]:
                self.priority_queue.insert(idx-1, value)
            elif value[1] >= elt[1]:
                self.priority_queue.insert(idx+1, value)
        assert sorted(self.priority_queue, key = lambda element: element[1])
        return

    def extract_max(self):
        highest = self.priority_queue[0]
        self.priority_queue = [elts for elts in self.priority_queue if elts != highest]
        return highest


max_q = MaxPriorityQueueMethod2()
max_q.insert((2, 0))
max_q.insert((4, 55))
max_q.insert((9, 5))
max_q.insert((8, 10))
max_q.insert((9, 0))
max_q.insert((3, 4))
max_q.insert((1, 5))
print(max_q.extract_max())
