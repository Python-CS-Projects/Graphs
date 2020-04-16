import random


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


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        # Create friendships
        for i in range(num_users):
            self.add_user(f"User {i + 1}")

        # all posible friendships
        posible_friends = []
        # nested loop O(n2) to create all posible combinations
        for user_id in self.users:
            for frien_id in range(user_id + 1, self.last_id + 1):
                posible_friends.append((user_id, frien_id))
        # Now the array of possible firendships has been randomize
        random.shuffle(posible_friends)

        # create n friendships where n = avg_friendships * num_users // 2
        #avg_firends = total_friendships / num_users
        #total_friendships = avg_friendships * num_users
        # Ex. 10 * 2 / 2 = 10 so it iterate from 0-10
        for i in range(num_users * avg_friendships // 2):
            # Assign friendship to each posible_friends in the array
            # each friendship = (X,Y)
            friendship = posible_friends[i]
            # print(f"Friendship: {friendship}")
            # add to friendship add_friendship(X, Y)
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Create queue
        q = Queue()
        # Enqueue path to user_id
        q.enqueue([user_id])
        # Visted diccionary
        visited = {}  # Note that this is a dictionary, not a set
        # While the q is not empty
        while q.size() > 0:
            # dequeue the first path
            current_path = q.dequeue()
            # Grab the last id from the path
            current_node = current_path[-1]
            # Check if it has NOT been visited
            if current_node not in visited:
                # Add it to the visited with the path
                visited[current_node] = current_path
                # Copy the path
                path_copy = current_path
                # Iterate over neighbors
                for friend in self.friendships[current_node]:
                    # Append each neighbor
                    path_copy.append(friend)
                    # Enqueue
                    q.enqueue(path_copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("Answer to Question 2A:")
    print(len(connections) / 1000)
    print("Answer to Question 2B:")
    total = 0
    for path in connections.values():
        total += len(path)
    print(f"Avg d= {total / len(connections) - 1}")
