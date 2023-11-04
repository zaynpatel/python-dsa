import heapq

class Vertex:
    def __init__(self, name):
        # Q: notice there's no "Node" instance in the Vertex class as there was in Kruskal's Algorithm - why is this?
        # A: One of the differences between Prims vs. Kruskal is the Prims algorithm begins with a vertex and grows the MST out of this vertex.
        # A: Whereas the Kruskal algorithm begins with "disjointed sets" and merges trees this way. There are Node characteristics important for Kruskal to work.
        self.name = name
        self.adjacency_list = []
        

class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex
    
    # __lt__ is a dunder method that "allows developers to define how built-in operations that are not custom objects, behave"
    def __lt__(self, other_edge):
        # compare the edge weights so we can get the ascending weight
        return self.weight < other_edge.weight 

class PrimsJarnikAlgorithm:
    
    def __init__(self, unvisited_list):
        self.unvisited_list = unvisited_list # stores all vertices except starting vertex
        self.mst = []
        self.total_cost = 0 # sum of the weights in the minimum spanning tree
        self.heap = []

    def find_spanning_tree(self, start_vertex):
        self.unvisited_list.remove(start_vertex) # we consider the start vertex visited when we begin the MST so we remove it. 
        actual_vertex = start_vertex 

        while self.unvisited_list: # what are we iterating through - isn't unvisited_list an int/what's it initialized too?
            # are we creating a list object for the actual vertex when we do this
            for edge in actual_vertex.adjacency_list:
                if edge.target_vertex in self.unvisited_list: # if we reach a node that we haven't visited, add it to the heap - what is self.heap doing when it's added herez?
                    heapq.heappush(self.heap, edge)
            
            # We're using a binary heap (special) that dequeues the smallest value, always
            min_edge = heapq.heappop(self.heap) # lazy implementation means we aren't removing the 

            # if the min_edge is unvisited, do we make it unvisited through this appending to the minimum spanning tree list?
            if min_edge.target_vertex in self.unvisited_list:
                self.mst.append(min_edge) 
                self.total_cost += min_edge.weight
                actual_vertex = min_edge.target_vertex # we select the next neighbor to traverse after we append one edge to the MST.
                self.unvisited_list.remove(actual_vertex) 