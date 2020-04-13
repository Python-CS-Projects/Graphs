
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
    # Initiate a path with the starting_node
    # Enqueue path
    # Create a set for visted
    # While queue is not empty
        # dequeue current path and save in var
        # *Think* Get last node in path [-1]
        # check if current node is not visited
            # add to visited
            # iterate on the current_node neighbors
                #Create a copy of the path
                #append neghbors to the path_copy
                #enqueue path_copy

    # 3.Initiate Graph with the ancestors list
    print(f"Vertices {vertices}")
    pass
