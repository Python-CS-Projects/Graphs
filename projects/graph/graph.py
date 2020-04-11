"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    # Adds a key+set() to the diccionary
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        this creates a diccionary of key + set()
        """
        # the value is saved in a diccionary to easyly access it
        # the set is use to store edges
        self.vertices[vertex_id] = set()

    # Add an edge between two vetices/nodes
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # v1_edges_set = the current key in the diccionary
        v1_edges_set = self.vertices[v1]
        # Adds the second value to the first value in the diccionary
        v1_edges_set.add(v2)
        # The result will be {Nodes/Vertices: (edges/relationships)}
        # we added to only one because is a directed edge and not both ways

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # Returns the set() of edges which are the neighbors
        if self.vertices[vertex_id]:
            return self.vertices[vertex_id]
        else:
            print(f"Node {vertex_id} does not exists.")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create queue
        q = Queue()
        # Enqueue/add the starting_vertex
        q.enqueue(starting_vertex)
        # Create a set ti tracj vertices we have visited
        visited = set()
        # While the queue is NOT empty
        while q.size() > 0:
            # Dequeue, the current vertex/node to deplete while loop
            current_node = q.dequeue()
            # If the current_node is not in the visited set()
            if current_node not in visited:
                print(current_node)
                # Add the current node/vertex to the set() of visited vertexes
                visited.add(current_node)
                # Now get the current_node's neighbors
                neighbors = self.get_neighbors(current_node)
                # iterate over the neighbors because is a set()
                for neighbor in neighbors:
                    # and add each to the back of the queue/line to keep running loop
                    # until we have visited all the neighbors
                    q.enqueue(neighbor)
        # When the queue is empty return set() of visited nodes = all nodes
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        The difference between bft and dft is
        here we use a stack instead of a queue
        O(Viteces + Edges) time complexity
        """
        # Create an empty stack
        stack = Stack()
        # Add the stating_virtex
        stack.push(starting_vertex)
        # Create a set to track vertices we have visited
        visited = set()
        # While the stack is empty
        while stack.size() > 0:
            # pop the  current_node and save in variable
            current_node = stack.pop()
            # If not yet visited
            if current_node not in visited:
                print(current_node)
                # Add/Mark as visited
                visited.add(current_node)
                # Get its neighbors
                neighbors = self.get_neighbors(current_node)
                # Iterate on neighbors
                for neighbor in neighbors:
                    # Push the neighbors to the stack
                    stack.push(neighbor)
        # Return visited
        return visited

    def dft_recursive(self, vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Because of how python works when setting default
        # is better to set the visited set as follow in case we call func mult times
        if visited == None:
            visited = set()
        # check if node has been visited
        if vertex not in visited:
            # Add to visited set()
            visited.add(vertex)
            neighbors = self.get_neighbors(vertex)
            # Base case not explicitly needed
            for neighbor in neighbors:
                # Call the func again and bring the visited to keep track
                self.dfs_recursive(neighbor, visited)

        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # Array of vetexes which are the path to destination
        # We use an array because order metters compare to a set() which is unordered
        path = [starting_vertex]
        # Add the path to the queue
        q.enqueue(path)
        # Create a set fo visited nodes
        visited = set()
        # While queue is empty
        while q.size() > 0:
            # Dequeue current_path, which returns the current_path to be analize
            current_path = q.dequeue()
            # Get the last node/value in the saved path
            # Python syntax for counting backwards [-1]
            current_node = current_path[-1]
            # check if current_node is detination_vertext
            if current_node is destination_vertex:
                return current_path
            # check if we have visited this node before
            if current_node not in visited:
                # Add to visited
                visited.add(current_node)
                # Get all neighbors
                neighbors = self.get_neighbors(current_node)
                # Iterate through neighbours
                for neighbor in neighbors:
                    # copy the current path
                    # python syntaxt to copy the entire path [:] or path.copy()
                    # we must copy because arrays are pass by reference
                    # so we dont want be adding to one array all the time
                    # we want separate arrays for each path
                    path_copy = current_path[:]
                    # add neighbor path copy
                    path_copy.append(neighbor)
                    # add copy to the queue
                    q.enqueue(path_copy)
        return path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a Stack
        # Add a path to starting_vertex
        # Create a Set to store visited Verteces
        # While the stack is not empty
            # Pop first path
            # Grab the vertex from the end (last one)
            # If it has not been visited
                # Mark as visited 
                # Check if is the target
                    # if true Return path
                # Add a path to all its neighbors to the stack
                    # Make a copy of the path
                    # Add the copy to the stack
        # return path
                




    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
