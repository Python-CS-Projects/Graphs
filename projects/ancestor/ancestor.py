# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_node):

    # 1.Create helper methods to Build Graph

    # iniciate vertices
    vertices = {}
    # Add Nodes
    for ancestor in ancestors:
        # print(ancestor[0])
        # Create vertices
        vertix_id = ancestor[1]
        vertices[vertix_id] = set()
    # Add edges
    for node in ancestors:
        vertix_id = node[1]
        vertix_2 = node[0]
        vertices[vertix_id].add(vertix_2)

    # 2.Create BFS

    # Create a queue
    q = Queue()
    # Initiate a path with the starting_node
    path = [starting_node]
    # Enqueue path
    q.enqueue(path)
    # Create a set for visted
    visited = set()
    # While queue is not empty
    while q.size() > 0:
        # dequeue current path and save in var
        current_path = q.dequeue()
        print(f"Current path {current_path}")
        # *Think* Get last node in path [-1]
        current_node = current_path[-1]
        # check if current node is not visited
        if current_node not in visited:
            # add to visited
            visited.add(current_node)
            # iterate on the current_node neighbors
            for neighbor in vertices[current_node]:
                print(f"Neighbor: {neighbor}")
                # Create a copy of the path
                path_copy = current_path
                # append neghbors to the path_copy
                path_copy.append(neighbor)
                # enqueue path_copy
                q.enqueue(path_copy)

    # 3.Compare paths to return the longest

    print(f"Vertices {vertices}")
    pass
