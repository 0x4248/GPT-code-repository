import time

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.location = 'start'

    def move(self, direction):
        if direction in current_room.exits.keys():
            self.location = current_room.exits[direction]
        else:
            print("You can't go that way!")

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def enter(self):
        print(self.description)

    def search(self):
        print("You search the room but find nothing of interest.")

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pick_up(self, player):
        player.inventory.append(self)
        print(f"You pick up the {self.name}.")

    def use(self):
        print(f"You use the {self.name}. Nothing happens.")

class Puzzle:
    def __init__(self, description, solution):
        self.description = description
        self.solution = solution

    def solve(self):
        print(self.description)
        guess = input("Enter your guess: ")
        if guess == self.solution:
            print("Congratulations! You solved the puzzle.")
        else:
            print("Incorrect solution. Try again.")

# Define game rooms
start_room = Room("Start Room", "You find yourself standing in a dark cave. There are two paths ahead, one leading left and the other leading right.")
left_room = Room("Left Room", "You enter a room filled with ancient artifacts. The air is musty, and you feel a sense of history surrounding you.")
right_room = Room("Right Room", "As you enter the room, you notice a glimmering treasure chest in the corner.")
final_room = Room("Final Room", "You have reached the heart of the lost city. A golden artifact rests on a pedestal in the center of the room.")

# Define room exits
start_room.add_exit("left", left_room)
start_room.add_exit("right", right_room)
left_room.add_exit("right", start_room)
right_room.add_exit("left", start_room)
right_room.add_exit("forward", final_room)

# Define game items
key = Item("Key", "A rusty key.")
treasure = Item("Treasure", "A chest full of valuable treasures.")

# Define puzzles
puzzle = Puzzle("Solve the riddle: What has keys but can't open locks?", "piano")

# Game initialization
player_name = input("Enter your name: ")
player = Player(player_name)
current_room = start_room

# Game loop
while current_room != final_room:
    current_room.enter()

    if current_room == right_room and treasure in player.inventory:
        print("Congratulations! You found the treasure and won the game!")
        break

    action = input("What would you like to do? ").lower()

    if action == "quit":
        print("Game over. Thanks for playing!")
        break

    elif action == "search":
        current_room.search()

    elif action == "pick up":
        if current_room == right_room and treasure not in player.inventory:
            treasure.pick_up(player)
        else:
            print("There is nothing to pick up here.")

    elif action == "use":
        if current_room == final_room and key in player.inventory:
            key.use()
            print("Congratulations! You have unlocked the artifact and completed your quest.")
            break
        else:
            print("There is nothing to use here.")

    elif action == "move":
        direction = input("Which direction would you like to go? ").lower()
        player.move(direction)

    elif action == "solve puzzle":
        if current_room == left_room:
            puzzle.solve()

    else:
        print("Invalid action.")

    print()

print("Game over.")
