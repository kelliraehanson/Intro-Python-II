from room import Room
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "book"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "map"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "sword"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "no items"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "puppy"),
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
print('\nHello there! Thanks for stopping by.\nHere is some helpful information:\n')
print('\n* Remember to explore the game by entering one of the following:\n\n[N] to go North\n\n[S] to go South\n\n[E] to go East\n\n[W] to go West\n\n[Q] to quit the game.\n')
print('\n* If there is an item in the room you are in, simply input:\n\n[GET] to take the item\n\n[DROP] to drop the item.\n')
new_player = input('What is your name? Please enter it here:\n')
player = Player(new_player, room['outside'], None)
print(f'\nWelcome to this game! Thanks for being here, {player.name}!\n')

def current_room(player):
    print(f'{player.name} you are currently in the {player.room}\n')
    print('\n* Remember to explore the game by entering one of the following:\n\n[N] to go North\n\n[S] to go South\n\n[E] to go East\n\n[W] to go West\n\n[Q] to quit the game.\n')
    print('\n* If there is an item in the room you are in, simply input:\n\n[GET] to take the item\n\n[DROP] to drop the item.\n')
    if player.room.items == 'no items':
        print('Sadly, this room has no items at the moment.\n')
    else:
        print(f'Look! This room has a {player.room.items}.\n')
        playerInput = input("-->\n").upper()

item_name = ""            

playerInput = ''
while playerInput != 'Q': 
    print(f'Hello, {player.name}. You are currently in the {player.room.name}.\n')
    print(player.room.description, "\n")
    print(f"Look! This room currently has a {player.room.items}.\n")
    print('* -------------------------------- *')
    # print(player)
    print('\n* Remember to explore the game by entering one of the following:\n\n[N] to go North\n\n[S] to go South\n\n[E] to go East\n\n[W] to go West\n\n[Q] to quit the game.\n')
    print('\n* If there is an item in the room you are in, simply input:\n\n[GET] to take the item\n\n[DROP] to drop the item.\n')
    playerInput = input("-->\n").upper()

    if playerInput == 'N' or playerInput == 'S' or playerInput == 'E' or playerInput == 'W':
        if playerInput == "N" and player.room.n_to != None:
            player.room = player.room.n_to
        elif playerInput == "E" and player.room.e_to != None:
            player.room = player.room.e_to
        elif playerInput == "S" and player.room.s_to != None:
            player.room = player.room.s_to
        elif playerInput == "W" and player.room.w_to != None:
            player.room = player.room.w_to
        else:
            print("Oh no, you can't go there! Pick another place to explore!\n")
    elif playerInput == "Q":
        print(f'\nGoodbye for now, {player.name}!\n')
        break
    elif playerInput == "GET":
        player.items.append(playerInput)
        print(f'Awesome, {player.name}! You picked up a {playerInput}.\n')
    elif playerInput == "DROP":
        player.items.remove(playerInput)
        print(f'Look at that, {player.name}! You just dropped the {playerInput}.\n')


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
# print('Enter "q" if you wish quit the game.')