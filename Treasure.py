import random


treasure_types = ["armor", "weapon", "food", "gold"]

food_types = [("a burger", 5), ("a pizza slice", 2), ("a chocolate", 3)]
weapon_types = [("a sword", 7), ("a dagger", 2), ("a shield", 6)]


class Treasure(object):

    # Constructor --> initializes a new Treasure object
    def __init__(self, kind):

        self.__kind = kind
        self.__is_carried = False
        self.__carrying = []   

        if self.__carrying != []:
            self.__is_worn = True
            
        if kind == "armor":
            self.__ac = random.randint(1, 11)
            self.__value = 20*self.__ac
            self.__is_worn = False
            self.__description = "an armor"

        elif kind == "weapon":
            weapon_kind = random.randint(0, len(weapon_types)-1) 

            self.__attack = weapon_types[weapon_kind][1]
            self.__value = 10*self.__attack
            self.__is_wielded = False
            self.__description = weapon_types[weapon_kind][0]

        elif kind == "food":
            food_kind = random.randint(0, len(food_types)-1) 

            self.__nutrition = food_types[food_kind][1]
            self.__value = 2*self.__nutrition
            self.__description = food_types[food_kind][0]
            
        elif kind == "gold":
            self.__description = "some gold"
            self.__value = random.randint(1, 30)

        self.__location = (-1, -1)
    

            
    def __str__(self):

        out_str = "ooops!!"
        
        if self.__kind == "armor":
            out_str = self.__description + " worth " + str(self.__value) + " gp"

        elif self.__kind == "weapon":
            out_str = self.__description + " worth " + str(self.__value) + " gp"

        elif self.__kind == "food":
            out_str = self.__description + " worth " + str(self.__value) + " gp"
            
        elif self.__kind == "gold":
            out_str = str(self.__value) + " gold coins"
            
        return out_str
        

    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return self.__location

    def pick_up(self):
        self.__is_carried = True


    def drop(self, location):
        self.__is_carried = False
        set_location(location)

    def wear(self, kind):
        
        if self.__is_worn == True:
            result = "You are already wearing armor"
        else:
            if self.__is_worn == False:
                self.__carrying.append(armor)
                result = "You are now wearing armor"

        return result

    def remove(self, kind):
        
        if self.__is_worn == False:
            result = "You are not wearing armor!"
        else:
            if self.__is_worn == True:
                self.__carrying.remove(armor)
                result = "You removed armor"

        return result

    def wield(self, kind):

        

        return result

    def unwield(self, kind):
        


        return result

    def eat(self, kind):
        


        return result
        
    def look_at(self):



        return result


