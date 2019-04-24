from room import Room
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Puppy", "A rescue puppy.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Book", "An old boring book.")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Walking stick", "Walking stick found near the overlook.")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Chamomile Tea", "To calm nerves")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Map", "A useful map.")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

new_player = input('Hello, what is your name? Please enter it here:\n')
player = Player(new_player, room['outside'])
print(f'Welcome! Thanks for being here, {player.name}!')

# Write a loop that:
#

# * Prints the current room name
    
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print('Enter "q" if you wish quit the game.')