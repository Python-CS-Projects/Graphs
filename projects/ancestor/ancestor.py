"""

Three steps to almost all graphs problems:

    1. Describe in terms of graphs

        Node = People
        Wdges = if they are parent-child

    2.Build our grphs

    3.Choose a graph algorithm

        Traversal or Search?
        There is no target only starting point, so we should use Traversal

        Breadth or depth?
        It works with both but we will use depth.
"""

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def add_edge(self, child, parent):
        self.nodes[child].add(parent)

    def getNeighbors(self, child):
        return self.nodes[child]


class Stack:
    def __init__(self):
        self.storage = []

    def pop(self):
        return self.storage.pop()

    def push(self, item):
        self.storage.append(item)

    def size(self):
        return len(self.storage)


def dft(graph, starting_node):
    stack = Stack()

    stack.push((starting_node, 0))
    visited = set()

    visited_pairs = set()

    while stack.size() > 0:
        current_pair = stack.pop()
        visited_pairs.add(current_pair)
        current_node = current_pair[0]
        current_distance = current_pair[1]

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.getNeighbors(current_node)

            for parent in parents:
                parent_distance = current_distance + 1
                stack.push((parent, parent_distance))
    longest_distance = 0
    aged_one = -1
    for pair in visited_pairs:
        node = pair[0]
        distance = pair[1]
        if distance > longest_distance:
            longest_distance = distance
            aged_one = node
    return aged_one


def earliest_ancestor(ancestors, starting_node):
    # build our graph
    graph = Graph()
    for parent, child in ancestors:
        graph.add_node(child)
        graph.add_node(parent)
        graph.add_edge(child, parent)
    # run dft
    aged_one = dft(graph, starting_node)
    # choose the most distant ancestor
    # run dft but track each path, then choose the longest path
    # run dft but add each node as a tuple (node, distance)
    return aged_one
