from room import Room
from player import Player
from item import Item, Light,Axe

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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


touchLight= Light("TouchLight","You have a light at hand, use it when needed", "off")
axe= Axe("Key","You can use the key to open the door", "not_use")
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player=Player(input("What is your name:"), room["outside"])
player.items.append(touchLight)
player.items.append(axe)


room['outside'].items=["axe","touchLight"]
room["narrow"].items=["water","mask"]
room["overlook"].items=["touchlight","ladder"]
room["foyer"].items=["trainers"]

print(player.current_room)
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
while True:
    print("You can go in the following direction [n,s,w,e]")
    user_input= input("In what direction do you want to go:")
    cmd=user_input.split(" ")
    if user_input=="q":
        exit(0)
    elif( user_input in ["n","s","w","e"]):
        player.travel(user_input)
        
    elif cmd[0]=="take":
        if cmd[1] in player.current_room.items:
            player.pick_item(cmd[1])
            player.current_room.items.remove(cmd[1])
            print(f"Item removed {player.current_room.items}")
            player.items.append(cmd[1])
            print(f"Item removed {player.items}")

    else:
        print("I don't understand that entry")
        
