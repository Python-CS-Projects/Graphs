from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Import Stack and Queue
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

"""
Solution:
We start at 0000 which is in the middle
Useful commands:
`player.current_room.id`
`player.current_room.get_exits()`
`player.travel(direction)`

Adjancency list:
{
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}
"""
# print(f"Rooms: {room_graph}")
# print("----------------------")
# print(f"Current room: {player.current_room.id}")
# print(f"Exits: {player.current_room.get_exits()}")
# print("----------------------")
# player.travel('s')
# print("Travel: South")
# print(f"Current room: {player.current_room.id}")
# print(f"Exits: {player.current_room.get_exits()}")
# print("----------------------")
print("----------------------")
print("Start of Solution.")
print("----------------------")


def reverseDir(dir):
    if dir == "n":
        return "s"
    if dir == "s":
        return "n"
    if dir == "e":
        return "w"
    if dir == "w":
        return "e"
    else:
        return None


def find_shortest_path(adj):  # BFS
    # Create an empty queue
    q = Queue()
    # Enqueue
    q.enqueue([player.current_room.id])
    # Create visited
    visited = set()
    # Loop
    while q.size() > 0:
        # get the path and dequeue
        path = q.dequeue()
        # Get the current node
        vert = path[-1]
        #If not in visited
        if vert not in visited:
            # Look for "?"
            if "?" in adj[vert].values():
                # print(f"Path: {path}")
                return path
            # Add to visited
            visited.add(vert)
            # Iterate over the neighbors
            for room in adj[vert].values():
                new_path = list(path)
                new_path.append(room)
                q.enqueue(new_path)
                # print(f"Room {room}")
                # print(f"Path {new_path}")
    return None


def get_dirPath(adj, path):  # Get the direccion coodinates n,s,w,e
    new_path = []
    # Iterate over the path
    for idx, room in enumerate(path):
        # print(f"IDX: {idx}")
        if idx > 0:
            lastRoom = path[idx - 1]

            for direction in adj[lastRoom]:
                if adj[lastRoom][direction] == room:
                    # print(f"Direccion: {direction}")
                    # Append the coodinate direccion
                    new_path.append(direction)
    return new_path


def travel_dir_path(traversal, path):  # Helper func to move to another room
    for direction in path:
        traversal.append(direction)
        player.travel(direction)


def create_traversal_path():  # DFT
    adjacency = dict()
    traversal = Stack()
    lastDir = None
    lastRoom = None
    while len(adjacency) < len(world.rooms):
        if player.current_room.id not in adjacency:
            adj = dict()
            # Iterate over the neighbors
            for ext in player.current_room.get_exits():
                # Add "?" to each direccion to use in BFS
                adj[ext] = "?"
            adjacency[player.current_room.id] = adj
        if lastRoom:
            # print(f"Last Room: {lastRoom}")
            adjacency[lastRoom][lastDir] = player.current_room.id
            adjacency[player.current_room.id][reverseDir(lastDir)] = lastRoom
        lastRoom = player.current_room.id

        # moved = False
        # for ext, room in adjacency[player.current_room.id].items():
        #     if room == "?":
        #         lastDir = ext
        #         traversal.push(ext)
        #         traversalPath.append(ext)
        #         moved = True
        #         player.travel(ext)
        #         break

        cur_adj = adjacency[player.current_room.id]
        unvisited = list()
        for direction, room in cur_adj.items():
            if room == "?":
                unvisited.append(direction)

        if len(unvisited) > 0:
            # Take ramdom direccion
            random.shuffle(unvisited)
            direction = unvisited[0]
            lastDir = direction
            traversal.push(direction)
            traversal_path.append(direction)
            player.travel(direction)
        else:
            # Get paths using BFS
            path = find_shortest_path(adjacency)
            if path is not None:
                # Get the coodinates direccion
                dir_path = get_dirPath(adjacency, path)
                # Travel to the direccion
                travel_dir_path(traversal_path, dir_path)
                lastDir = dir_path[-1]
                lastRoom = path[-2]

        # if not moved:
        #     ext = reverseDir(traversal.pop())
        #     traversalPath.append(ext)
        #     lastDir = ext
        #     player.travel(ext)
lowest = 999999
shortestPath = []

for i in range(10000):
    player.current_room = world.starting_room
    traversal_path = []
    create_traversal_path()
    if len(traversal_path) < lowest:
        lowest = len(traversal_path)
        shortestPath = traversal_path

traversal_path = shortestPath
print(shortestPath)


print("----------------------")
print("End of Solution.")
print("----------------------")

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
