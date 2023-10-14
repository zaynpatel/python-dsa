### what are associative arrays
Associative arrays are an abstract data type meaning they define a behavior without the implementation. They use key:value pairs where keys appear at most once in the collection and they're able to achieve a constant running time *if* we know the key we'd like to retrieve. We use associative arrays because they offer quick runtime for these operations.

### hashtable introduction - basics

The operations we can do with associative arrays are: add, remove, search/lookup. We can't sort because key:value pairs are unordered. When we know the index of the key:value pair, we can get O(1) running time. The way to achieve this is by using an array with random access and this is done by the hash function or what I'll reference as `h(x)`.

The hash function *map keys to an index in the range from 0 to m-1 where m is the size of the table*. Hash functions handle any type. For strings, we use ASCII conversion to convert the string into numbers, then we add the numbers and use modulo division to divide by the len(hashtable). The output gives us an index number where the key:value pair will be inserted into. 

### hashtable introduction - collisions
One of the problems with the insertion of a key:value pair into an array is collisions. In other words, there might be two string values where the sum (and modulo division) of their ASCII values is the same so the index they'll be inserted into is also the same. This leads to a problem where we have to decide to override the current value in the array or discard the new value calculated. Neither of which are optimal for storing data. So, we use "collision handling" to move items around so this issue doesn't happen. 

There are two defined ways of doing this: chaining and open addressing. Chaining involves the linked list data structure where values that resolve to the same index are placed there, with pointers to the other values of the same index. This is less common because in the worst case, it can become a linked list with O(n) running time. This running contradicts the ideal constant running time behavior behind using hash tables is to achieve O(1) running time for operations like add, remove, search. Open addressing involves finding a new place in the array to place the key:value pair. This includes linear probing where a value increments in index to find another free index to be placed. Quadratic probing which increments at x^2. There are tradeoffs for both of these methods. 

In linear probing, the values are close to each other in memory so searching is quick but there are clusters of values that form. This is bad because if there's a new element to place, it becomes difficult to do so without copying the entire array and starting again. Whereas in quadratic probing, the values are farther apart but search becomes faster because of this. 

### hashtable introduction - dynamic resizing

Load factor is used for new parameters of hash table specifically. *The formula for this is n / m where n = the number of items in the array and m = amount of memory allocated for the array (also, what are the total indices for this?). This helps us determine how empty or full a hash table is. A small load factor, around 0, means the hash table is empty so there's memory that's wasted. But, it also means the probability of collisions is lower because there are less items to collide with. 

A large load factor is the opposite where more memory is used and the probability of collisions is higher. Both Java and Python use a technique called dynamic resizing which monitors the load factor and if it's above a threshold (0.75 for Java, 0.66 for Python), the values are ported to a new array that's a larger size. This is O(n) running time. 

### Why to use prime numbers in hashing
By using prime numbers for hash functions, keys tend to be distributed uniformly and this can help in reducing collisions as they're less likely to share factors with other numbers. *Composite numbers have more divisors so collision patterns are more likely.*