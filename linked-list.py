# Coding Exercise 5 in course - find the middle of a linked list
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0

    # this is the part I did by myself, figuring it out!
    # O(N) linear running time complexity
    def get_middle_node(self):
        tortoise = self.head
        hare = self.head

        # before running the while loop I need to check if the the linked list has elements or if it's empty since there's no middle node to get in this case
        if self.head == None:
            return None
        
        # check whether the next node is not None because we're searching for the end of the linked list and if we have hare is None, we could have an error since we're looping through
        # the self.head and updating the next_node. We could iterate our way to an IndexError, I think.
        while hare.next_node is not None:
            if hare.next_node and hare.next_node.next_node is None:
                # add a break statement to get out of the loop if we are at the end of the list so we know to move forward
                break
            else:
                hare = hare.next_node.next_node
                tortoise = tortoise.next_node

        return tortoise

    def insert(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse_list(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node
 
 
class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

# Coding Exercise 6 - Reverse a linked list in-place exercise
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # this is the part I did myself, figuring it out!
    # O(N) linear running time complexity
    def reverse(self):
        # there are three pointers I'm going to use to reverse this in space
        prev = None
        # the while loop deals with current since this is the node we're actively working with, prev and next_node exist to modify the pointers
        current = self.head
        next_node = None

        while current is not None:
            # the next node after head is the next node, so if I have a linked list 1 -> 2 -> 3 -> 4, the next node is 2
            next_node = current.next_node
            # then I want to set the pointer here to be the previous, so now it's 1 <- 2 -> 3 -> 4
            current.next_node = prev
            prev = current
            current = next_node
        
        self.head = prev


    def insert(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
            
    def get_head(self):
        return self.head

    def traverse_list(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node