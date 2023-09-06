### What are stack data structures?

They are an abstract data type which means "we know what operations are available and what kinds of behavior these operations should have", however, it's not specified how these operations are implemented. In stacks, for example, operations include: `push()`, `pop()`, `peek()` and in queues there is `enqueue()` and `dequeue()`. 

Stacks operate with a "Last in First Out (LIFO)" principle which gives us a structure for how to access items in a stack. For example, if we have a 2D list [[3, 4, 5], [5, 8, 10]] and I want to access the last item in both lists, I'll call s.pop() in a for loop and can get both 10 and 5. If I want to access just 10, I can implement a nested loop that looks at both lists specifically and calls the .pop() method on the second list with 10 in it. 

Stack memory is an example of where the stack data structure is useful. Stack memory has a special region in RAM (Random Access Memory) that's specifically for the program's stack which includes space for the (a) code and (b) variables. Stack also stores local variables that are needed for the program's execution and "cleans them up" or gets rid of them after use. 

### Heap memory vs. stack memory

Heap memory is typically for storing dynamically allocated variables. This means objects, lists, data structures where I can add or delete items as I'm writing a program. This includes appending items to a list, removing them from a list too. Stack memory is for storing local variables, function calls. 

The bookkeeping methods of these memories are different. Stack memory involves pointer movement. If I want to change whether something is allocated or deallocated, I can do so by changing the stack pointer. In the case of heap memory, this is more complex (and remains an open question for me to figure out).

Size is different. Stack memory allocates size at the beginning of a program whereas heap memory grows size during runtime. 

### What are queue data structures?
Queues have a First In First Out (FIFO) data structure. I implemented them from scratch [in this python file](/Users/zaynpatel/Python-DSA/python-dsa/stacks_queues/stacks_queues.py). The structure of it is simple, it can remove or add the first item of a list. Because it can only access the first item, dequeuing has an O(N) running time since it has to iterate through all elements of the list before being able to remove or `del` an item.  


### Remaining questions
- How will a programmer know if they're at stack overflow or reaching this point?