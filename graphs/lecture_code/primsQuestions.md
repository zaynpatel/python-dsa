### Quiz Questions for Prim's Algorithm
*Italics in the answer represent clarifications, most on precision of the response.* 


Question 1: Why do we use a min-heap in Prim's algorithm. 
Answer 1: We use this data structure because our goal is to access the node with the smallest edge weight since we're trying to get a minimum spanning tree as an output. I believe binary heaps are the only data structure that allows us to access this element exclusively. It has operations built in like .pop() so we can get the minimum value.

Question 2: The heap operations contribute to O((V + E) log V) Why can we simplify the overall complexity to O(E log V) or O(V log V) in some representations?

Answer 2: Instead of thinking about the expression O(( V + E) log V) which is a correct way to think about the time complexity, just a little bulkier, we can think about the fundamental requirements of a graph. Ie - *A connected graph has at least V - 1 edges, so the number of edges E is bound to be greater than or equal to V - 1.* Every operation in the heap is O(log V)time because we need to maintain the heap structure. *We consider each edge once when we examine all neighbors for the vertex and this gives us O(E). Each heap operation, as mentioned above takes O(log V) so we multiply these together to get O(E log V)*.

Question 3: How would you describe the process of "relaxing an edge, and why is it important to the algorithm's operation?"
Answer 3: Edge relaxation is defined examining an edge to see if it offers a better path to a node. The process of relaxing an edge in Prim's Algorithm happens by a vertex examining the surrounding edge weights and after it's completed this, it examines which edge will keep the total cost down. This is important to the algorithm because we can have more than one vertex with an edge to toe other and by considering all neighboring paths and then choosing the smallest, we can ensure we're finding the min spanning tree. 

Question 4: Can you explain the property of a min-heap that allows the minimum element to be accessed in O(1) time? How does this affect algorithm's efficiency?
Answer 4: The heapify operation is the property of a min-heap that allows it to be accessed in O(1) runtime. For a min-heap, the operation takes in an edge weight(s) and sorts them. The process moves like this: insert, check the root node to see if it's less than or greater than since this determines the side it's on. Then, check the parent node and see if it's greater than this or not. If yes, insert. If no, keep traversing. This ensures that the value that's minimum is always near the top. 

Question 5: Prim's algorithm can be implemented using an adjacency list or an adjacency matrix. How would the choice between these two representations affect the algorithm’s performance?
Answer 5: We typically use adjacency lists for problems where we want to represent sparse (or smaller) graphs. They have less space complexity if I recall correctly because, in the case of adjacency matrices we store V^2. This is better for denser graphs. 

Question 6: Contrast lazy implementation with eager implementation. How do they handle edges and update the heap?
Answer 6: *In the lazy version, edges that are not the smallest can accumulate in the heap, while the eager version updates the heap more aggressively by immediately discarding edges that are no longer valid. This keeps the heap smaller and can result in improved performance because the heap operations are less costly due to fewer elements in the heap.*

Question 7: Are there any types of graphs or specific conditions where Prim's algorithm might not be the best choice for finding a minimum spanning tree?
Answer 7: Not suited for disconnected graphs because it can't span across components. Also  less efficient for dense graphs because it's represented using an adjacency list.

Question 8: If we didn't have a heap available, how might we modify Prim's algorithm to still work efficiently? What trade-offs would we have to consider?
Answer 8: *We can use an array but this means O(V^2) time complexity. BST's can help with O(log n) insertion and deletion but we lose O(1) lookup.* Note that all self-balancing trees maintain order which is why we lose O(1) runtime. 