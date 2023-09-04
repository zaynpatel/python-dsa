### What are doubly linked list data structures?
Doubly linked lists are linked lists with two pointers (one to the previous node and one to the next node). This is better than traditional linked lists which only have a pointer to the next node.

In linked lists, searching for the head node contains an O(1) running time because we store a reference to it; in doubly linked lists, we store the head and tail node because it permits us to append and remove nodes from either side without hassle. *One of the disadvantages of linked lists is having to traverse the list to add a data point to the end.* This is prevented using doubly linked lists. 

Note: insertion of linked list points can happen anywhere (beginning, end, middle). Removing nodes is easier because of two pointers too. 

One of the disadvantages of doubly linked lists is, they require more memory b/c of two references (2 pointers).

### Implementation differences

- `def __init__` in doubly linked lists initializes two nodes (previous and next) instead of linked lists which initialized one node (next).



### Running question list
- Algorithms like binary search exist to search through new data structures quicker and we use new data structures to store data in ways that benefit our application more. Ie - linked lists and photo image storer or bitcoin. These d/s are mutations of dicts and lists but provide new functionality. 