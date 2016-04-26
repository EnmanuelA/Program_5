from Treasure import *
from Player import *


import random


EMPTY = "."
WALL = "#"
UP_STAIRS = "u"
DOWN_STAIRS = "d"
TREASURE = "*"
PLAYER = "P"
MONSTER = "M"

class Level(object):    

    def get_new_empty_location(self):

        is_empty_cell = False
        while not is_empty_cell:
            x = random.randint(1, self.__width-2)
            y = random.randint(1, self.__height-2)

            if self.__grid[y][x] == EMPTY:
                is_empty_cell = True
            # if the self.__grid cell at (x, y) is not empty, roll again
                
        return (x, y)

    # create a level
    def __init__(self):
        # these should be done randomly.  So far hard-coded
        self.__width = random.randint(10,40)
        self.__height = random.randint(15,20)
       
        # create self.__grid
        # create horizontal wall
        wall_line = self.__width*WALL
        middle_line = WALL + (self.__width-2)*EMPTY + WALL

        self.__grid = [wall_line]    
        for row in range (1,self.__height-1):
            self.__grid.append(middle_line)
        self.__grid.append(wall_line)

        # create stairs
        (self.__up_x, self.__up_y) = self.get_new_empty_location()
        line = self.__grid[self.__up_y]
        line = line[:self.__up_x] + UP_STAIRS + line[self.__up_x+1:]
        self.__grid[self.__up_y] = line
        
        (self.__down_x, self.__down_y) = self.get_new_empty_location()
        line = self.__grid[self.__down_y]
        line = line[:self.__down_x] + DOWN_STAIRS + line[self.__down_x+1:]
        self.__grid[self.__down_y] = line

        # create treasure
        # random number of piles
        number_piles = random.randint(5, 10)
        self.__treasure_list = {}

        for pile in range (0, number_piles):
            # create a treasure pile
            number_treasures = 3
            treasure_pile = []

            # repeat 
            for k in range(0, number_treasures):
                # select randomly the object's type
                kind = random.randint(0, len(treasure_types)-1)
                # create the object
                my_object = Treasure(treasure_types[kind])
                # add to the list
                treasure_pile.append(my_object)

            # random location or pile
            (x, y) = self.get_new_empty_location()
            line = self.__grid[y]
            line = line[:x] + TREASURE + line[x+1:]
            self.__grid[y] = line

            self.__treasure_list[str((x,y))] = treasure_pile


    # display the current level self.__grid
    def __str__(self, player):

        (player_x, player_y) = player.get_location() 

        outStr = "\n\n"
        for row in range(0, self.__height):
            if row != player_y:
                outStr += self.__grid[row] + "\n"
            else:
                line = self.__grid[row]
                line = line[:player_x] + PLAYER + line[player_x+1:]
                outStr += line + "\n"
        outStr += "\n"
        return outStr


    # display the current level self.__grid
    def print_level(self, player):

        (player_x, player_y) = player.get_location() 

        outStr = "\n\n"
        for row in range(0, self.__height):
            if row != player_y:
                outStr += self.__grid[row] + "\n"
            else:
                line = self.__grid[row]
                line = line[:player_x] + PLAYER + line[player_x+1:]
                outStr += line + "\n"
        outStr += "\n"
        print(outStr)


    def get_up_point(self):
        return (self.__up_x, self.__up_y)
    
    def get_down_point(self):
        return (self.__down_x, self.__down_y)

    def is_valid_location(self, x, y):
        return self.__grid[y][x] != WALL

    
