# Problem 1: Implement depth-first search using recursion
# Date: October 19, 2023 (120)

class Node: # serves as a blueprint for creating node objects - I can instantiate nodes w/these objects as done below
    def __init__(self, name): # we put a parameter in the input params when we want to uniquely identify something/initialize it once and use in rest of code
        self.name = name
        self.visited = False # default state
        self.adjacency_list = [] # what we're looping through
"""
One way to append items to the Node class is:
node_z = Node("Zayn")
node_p = Node("Patel")

node1.adjacency_list.append(node2)
"""

# "aha moment" - notice that we don't need an explicit stack in the recursive definition vs. iterative which does require it. this is because recursive has stack memory built-in so it will complete the DFS according to its needs. 
def depth_first_search(start_node):
    print(f"Attempting to visit {start_node.name}")
    # base case is they are all visited
    if start_node.visited is True: # make sure it's `start_node.visited` - had to correct this after an error. We want to reference the object of visited/not instead of the value `start_node`
        print(f"{start_node.name} already visited.")
        return 
    else:
        print(f"Visiting {start_node.name}") 
        start_node.visited = True # relocated so the node is marked as visited *right* before it's going to visit neighbors
        # ^ this was previously defined inside the for loop and it meant I was marking it as visited without exploring all neighbors so it wasn't completing a successful search
        # ^ lesson in "be cautious where the statement is defined" and what behavior this makes the program do
        for n in start_node.adjacency_list:
            if not n.visited:
                print(n.visited)
                depth_first_search(n)

# Create nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")

# Create edges (this is an undirected graph)
nodeA.adjacency_list = [nodeB, nodeC]
nodeB.adjacency_list = [nodeA, nodeD]
nodeC.adjacency_list = [nodeA, nodeD]
nodeD.adjacency_list = [nodeB, nodeC, nodeE]
nodeE.adjacency_list = [nodeD]

# Perform depth-first search starting from node A
depth_first_search(nodeA)

# Problem 2 - BFS to find way out of maze
# Date: October 20, 2023
"""
[
   [S, 1, 1, 1, 1],
   [0, 1, 1, 1, 1],
   [0, 0, 0, 0, 1],
   [1, 0, 1, 1, 1],
   [0, 0, 0, 1, D]
]
The (0,0) is the source and (4,4) is the destination. 
0 represents walls or obstacles and 1 is the valid cells we can include in the solution.
"""

"""
Learnings:

- List comprehensions are good for initializing something the same dimension. Writing [[False]] * len(maze) would've given you [[False], [False], [False]], for example which aren't the dimensions of the maze.
- Queues are helpful because we can go level by level exploring neighbors and marking vertices as visited.
- We can write for loops like this: for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]: <- Ie - we can have a list of all neighbors to iterate through
- In this problem, we don't need to access the individual values of the maze, we can instan. store_bool and use this. What we care about is, where did we start, what have we visited, and where do we end. 
We don't care as much about traversing the maze as much as we do the criteria mentioned above. 
"""

def breadth_first_search(maze):
    # initialize the items
    # the store_bool list comp is defined so we can iterate on the 2D list (columns) based on the number of rows there are in the maze
    store_bool = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))] # initialize a 2D list that has False for all values the length of the maze matrix
    start = (0, 0) # make these coordinates since this is where, in the 2D list, we're starting. Better than maze[0][0] which would give me a value
    destination = (4, 4)
    queue = [start]

    # start the search
    while queue: # no need for a for loop because queue itself acts as a loop iterator
        actual_node = queue.pop(0)
        i, j = actual_node 
        store_bool[actual_node[0]][actual_node[1]] = True # after the dequeue is when we want to mark elements as True. Can't do this before hence why it doesn't work inside the if statements

        if actual_node == destination:
            print("Reached.")
            break


        if i + 1 < len(maze): # check for bounds of neighbors
            # removed == False and replaced with not since more pythonic
            if not store_bool[i + 1][j] and maze[i + 1][j] == 1: # this check is to see if the cell has already been visited or not
                queue.append((i + 1, j)) # append the index to the queue because this will tell the queue where to look next
        if i - 1 >= 0: # useful to check to make sure we're not wrapping around list
            if not store_bool[i - 1][j] and maze[i - 1][j] == 1:
                queue.append((i - 1, j))
        if j + 1 < len(maze[0]):
            if not store_bool[i][j + 1] and maze[i][j + 1] == 1:
                queue.append((i, j + 1))
        if j - 1  >= 0:
            if not store_bool[i][j - 1] and maze[i][j - 1] == 1:
                queue.append((i, j - 1))