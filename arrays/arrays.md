### What are array data structures?

Arrays store items in an index which gives an "id" to each element so it can be accessed. Because indexes exist, we can add or remove elements via index. 

In typical array data structures, elements are next to each other in the RAM. This is an advantage because it keeps the runtime at O(1) meaning, for any increase in elements, the runtime stays constant (nothing happens to it).

To calculate the memory address of an array, we'll use: `memory address = array's address + index * data size (4 byte)`. 

Lists in Python are different from arrays in a few ways. The **first** is, they don't store the actual data like an array does, instead it stores a reference to the data. In Python, everything is an object so we can think about this like, every object in a list has a reference. There was a demo of how lists are written in Python and it's written in C, where `**obclaim` is the pointer. Because every object is a reference, all objects can be stored and they're all 8 bytes, no matter the type. The number of bytes required for each object is one of the reasons why lists have huge memory complexity. In C, ints are stored as 4 bytes w/variable bytes for other types. 

Anyway, when Python takes a list like `name = ['zayn', 'patel']` it stores these anywhere in memory but uses a common memory address so the Python interpreter knows where that the two elements in my name. Name is a reference to a list object and 'zayn' and 'patel' are references to string objects. The list object is what connects these two. When I'd like to access, Python finds the referenced memory address and returns the string object I'm requesting. 

Lastly, this is why `np.array` is useful - it is the only way to create arrays in Python. Times when I'll want to store similar objects in contigious memory, this will be helpful. 

Note: there is memory overhead (excess computation time) by using Python lists because the first step is to access the reference, the second step is to access the object at that reference. Also note that the runtime for accessing is O(1) and O(n) for inserting/deleting. There isn't a difference in programming language or array/list. Both require iterating through elements and shifting their position. 

There is a tradeoff between space (memory) and time(speed of algorithm running) when writing code. In arrays, specifically, we have a tension of allocating 2X the RAM for an array so we can allocate more data at available indexes but this wastes memory if it's not used. Or, we can allocate a small amount of memory and if we need to allocate more in the future, perform an O(n) operation where we shift the current data by N. 

Note: We end up with an O(N) algorithm when dealing with arrays *when we insert items at the beginning of an array* because, we shift everything else by the number of elements there are. 

### Implementation learnings
When implementing the reverse(), I learned that Python in-place operations produce None becuase they're modifying the object in place but not producing a new object. Difficult to know whether an operation is in-place or not (look for a return value & if you don't find one, look at documentation). 

`copy()` method is how you clone a dtype. 

When you see `s[left]` or `s[right]` in the second array problem, recall that this means we want to access characters at a specific indices. 

For number 3, there's an interesting approach taken to reversing integers. Because integers are not strings (and can't be sliced), we need to convert integers into a form that allows for us to access digits. 

The method that's common is to take the input integer, like `1234` and multiply it by 10, extracting the remainder. 

It works like the following: 

```
Iteration 1: result = 0 * 10 + 4 = 4, n = 123
Iteration 2: result = 4 * 10 + 3 = 43, n = 12
Iteration 3: result = 43 * 10 + 2 = 432, n = 1
Iteration 4: result = 432 * 10 + 1 = 4321, n = 0
Return 4321
```

### Running question list
- What format of code allows runtime to be constant, logarithmic, etc? 
- Do people use np.array() if they want a traditional comp. sci array instead of python lists?
