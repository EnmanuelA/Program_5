from Treasure import *
from Level import *



class Player:

    def __init__(self, current_level):

        self.__displacements = {"h":(-1, 0), "k":(0,1), "j":(0,-1), "l":(1,0)}
        self.__current_level = current_level
        
        self.__location = current_level.get_up_point()
        
        # the player comes with nothing to the world
        self.__inventory = []
        # health is 100 when we first start
        self.__health = 100

    def move(self, command):
        if command == "h":
            (dx, dy) = (-1, 0)
        elif command == "k":
            (dx, dy) = (0,1)
        elif command == "j":
            (dx, dy) = (0,-1)
        elif command == "l":
            (dx, dy) = (1,0)  
            
 #      (dx,dy) = self.__displacements(command)
        new_x =  self.__location[0] + dx
        new_y =  self.__location[1] + dy

        # ask if new location is good
        if self.__current_level.is_valid_location(new_x, new_y):
            self.__location = (new_x, new_y)
            outStr = "OK"
        else:
            outStr = "You can't go there"
        return outStr

    def set_location(self, location):
        self.__location = location
        
    def get_location(self):
        return self.__location

    def pick_up(self, obj):
        # add the object to inventory
        self.__inventory.append(obj)
        print("You picked up and object")
        obj.pick_up()


    def print_inventory(self):
        obj_index = 1
        for obj in self.__inventory:
            print("(" + str(obj_index) + ")\t" + str(obj))
            obj_index += 1


    #-------------------------------------
    #        to be done
    #-------------------------------------


    def look_at(self):



        return resultStr

    def eat(self, obj_index):



        return resultStr


    def drop(self, obj_index):
        resultStr = "You can't drop that!"
        
        # make sure that the index is valid.  If it is,
        # then update inventory, object status, and
        # change return to --> You dropped [object description]

        return resultStr


    def wear(self, obj_index):
        resultStr = "You can't wear that!"
        
        # make sure that the player is not already wearing.
        # make sure that the index is valid.  If it is,
        # then update inventory, object status, and
        # change return to --> You now wearing [object description]

        return resultStr

    def remove(self):
        resultStr = "You are not wearing anything!"
        
        # make sure that player is wearing an armor. 
        # then update inventory, object status, and
        # change return to --> You removed [object description]

        return resultStr

    def unwield(self):
        resultStr = "You are not wielding anything!"
        
        # make sure that player is wielding a weapon. 
        # then update inventory, object status, and
        # change return to --> You removed [object description]

        return resultStr

    def equip(self):
        resultStr = "OK."
        
        # make the player wear the first armor on inventory list
        # (if not already wearing one) and wield the first weapon
        # on the inventory list (if not already wielding one).

        return resultStr
        


