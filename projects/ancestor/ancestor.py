
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
    # get neighbors

        # 2.Create BFS

        # 3.Initiate Graph with the ancestors list
    print(f"XXX {vertices}")
    pass
