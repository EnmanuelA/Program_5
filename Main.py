
from Treasure import *
from Player import *
from Level import *

# the current_level variable will all store the level the
# player currently is at
current_level = Level()
level_list = [current_level]



my_player = Player(current_level)

current_level.print_level(my_player)

# main loop
ongoing_game = True
while ongoing_game:

    user_input = input("enter command: ")

    #  get user command
    if user_input == "h" or user_input == "j" or\
       user_input == "k" or user_input == "l":
        # if grid square to the left is within bounds
        result = my_player.move(user_input)

    current_level.print_level(my_player)

