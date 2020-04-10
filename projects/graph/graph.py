"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        v1_edges_set = self.vertices[v1]
        v1_edges_set.add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()
        # Enqueue the stating_virtex
        q.enqueue(starting_vertex)
        # Create a set ti tracj vertices we have visited
        visited = set()
        # While the queue is empty
        while q.size() > 0:
            # Dequeue, this our current_node
            current_node = q.dequeue()
            # Mark as visited
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                # Get its neighbors
                neighbors = self.get_neighbors(current_node)
                # and add each to the back of the queue
                for neighbor in neighbors:
                    q.enqueue(neighbor)
        # Return visited
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        The difference between bft and dft is
        here we use a stack instead of a queue
        O(Viteces + Edges) time complexity
        """
        # Create an empty queue
        stack = Stack()
        # Enqueue the stating_virtex
        stack.push(starting_vertex)
        # Create a set to track vertices we have visited
        visited = set()
        # While the queue is empty
        while stack.size() > 0:
            # Dequeue, this our current_node
            current_node = stack.pop()
            # Mark as visited
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                # Get its neighbors
                neighbors = self.get_neighbors(current_node)
                # and add each to the back of the queue
                for neighbor in neighbors:
                    stack.push(neighbor)
        # Return visited
        return visited

    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if vertex not in visited:
            visited.add(vertex)
            neighbors = self.get_neighbors(vertex)
            # Base case not explicitly needed
            for neighbor in neighbors:
                # Call the func again
                self.dfs_recursive(neighbor, visited)

        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        print("XXX Start bfs XXXX")
        # Create an empty queue
        q = Queue()
        # Enqueue the stating_virtex
        q.enqueue(starting_vertex)
        # Create a set ti tracj vertices we have visited
        visited = set()
        # While the queue is empty
        x = True
        while q.size() > 0:
            # peek at head
            current_node = q.dequeue()
            n = self.get_neighbors(current_node)

            if destination_vertex in n:
                print("Got it")
                q.enqueue(n)
            q.dequeue()
        print(f"Result {q}")
        # for x in current_node.edges:
        # print(x)

        print("XXX End bfs XXXX")

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

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
