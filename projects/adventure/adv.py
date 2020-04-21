from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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

# Graph
graph = {}
# Add "?" to the exits


def pre_graph():
    # Initialize the nested diccionary
    graph[player.current_room.id] = {}
    for x in player.current_room.get_exits():
        # Add "?" to each exit
        graph[player.current_room.id][x] = "?"


pre_graph()
print(graph)
# Create a DFT

# BFS to search for rooms with a question mark

# BFS will return a list of id's we need to convert to coordinates

# if all paths has been explored then return the list append to traversal_path


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
