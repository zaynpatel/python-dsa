### What are linked list data structures?
The link list data structure is a list that contains pointers as references to different notes. The head node is initiated as its own object `self.head`. It's helpful because there remains a starting point to traverse the list through. The last node points to NULL; this is how we know where the list ends and its length. 

Linked lists are helpful over arrays because we can insert and delete by chancing the pointer to another memory address. We don't need to shift all items. The data structure has an O(n) running time because although it's easier to add and delete, searching requires traversing all data/pointers. Hence the `self.next` object. Linked lists have take up more memory than arrays because they store the data and the reference to the next node. Lists, in python, just store the reference not the data so it takes more memory than this too. 

Head node adjustments in linked lists are simple since it requires an update of the references, the code in C is, `list.FirstNode = newNode`. A renaming is all it takes whereas when we want to add/delete something from the last node we have to iterate through the list until we find null. The C code is, `while node is not null`. 

**Pros:**
- Linked lists are dynamic data structures so they can aquire memory at run-time without needing to resize. One of the problems with arrays is the need to resize the list for new elements at the beginning, middle, or end. 

**Cons:**
- No backwards pointer
- No random access, can only access through head node

### Running question list
- Why are hexademical vs. bytes useful as a thing to know? 
- What is the structure of memory address?
- What's the avg memory for dtypes (int, str, char, obj) and data structure (lists, dicts)?