### What are binary search trees?

- To get optimal performance from a binary search tree, two things need to be true: (a) the tree is balanced (there are an approximate number of nodes on each side of the tree where the left side contains items that are smaller than the root node and the right side contains items that are greater than the root node. Smaller and larger are somewhat ambiguous in this statement but it refers to the way items are sorted in the tree. For example, I could have a list of names: Zayn Patel, MacBook Air, iMessage, AirPods and I define the order these should be sorted in. I think this is correct. A core element of binary search trees is that they're sorted. If they weren't sorted, it would be difficult to search and try to find the middle value since there's no order to what the middle value is besides the length of the tree). 

- The height of a binary search tree is based on the formula 2^(h)-1 which looks at how many levels there are in the tree. I suppose this is important to calculate the fact that the runtime is O(logN). The ideal is to keep the height of the tree at a minimum so the number of nodes to search for doesn't increase out of hand. 

- Insert in binary search trees appear to be simple. Looks like it's mostly conditonal flow to see what is greater than the other and then inserting the items into the tree. 

- Search is done by checking the root node, then seeing whether the value we're searching for could be on the left or right side. Depending on its value, we cut off half the tree and proceed to search based on the node splits. 

### Deleting nodes in a binary search tree

There are three methods:

First: Removing a leaf node is simple, we remove the reference to it. Unlike linked lists where we'll change the reference to NULL, it's deleted in this data structure. 

Second: Removing a node with a single child means changing the reference from the root node to the new node. For example: 32 (root node) -> 55 (parent node) -> 79 (child node) and I want to remove the parent node (55), I can update the reference from 32 -> 79 so 79 becomes the parent node and 55 is removed. 

Third: Removing a node with two children. This is harder because it involves using other nodes (successor (node with minimum value in right subtree) and predecessor (nod with the maximum value in the left subtree) -- the first principles of this is: if I replace the tree with another node, the tree won't be searchable via BST) such that the node we want to remove becomes a leaf node and it's replaced by a predecessor or successor that keeps the binary search tree in tact. 

### Types of tree traversal in BST

There are three methods:

**Method 1:** The first method is called a pre-order traversal which includes visiting the root node, left subtree, and then the right subtree. The use cases of this method include (a) creating a deep copy of the tree because this traversal searches the tree from scratch in a top-down manner. One of the ways to remember the pre-order traversal is (DLR which means Data-Left-Right). Data is the root node and the left/right refer to those subtrees. A helpful analogy if you're trying to explain how you're learning something is to say via a pre-order traversal since you're beginning at the top concept and working your way down by traversing the sides of knowledge. (b) is for prefix notation which includes the operator at the beginning of an expression `+ 3 4` instead of `3 + 4`. Pre-order traversals can be used here because when the tree works from the top to bottom it will see the operands before the numbers. 

Note: Some compilers use prefix notation to understand the operation. Can work with stacks too - add numbers to the stack, see the operand. Pop them off, add them back and the expression is evaluated. 

**Method 2:** The second method is post-order traversal which includes visiting the left subtree, right subtree, and root node. 

**Method 3:** The third method is the in-order traversal which includes visiting the left subtree, root node, right subtree. This is helpful to confirm the tree you're working with is a BST since it searches all nodes in the left subtree, then looks at root node, and then the right subtree. 