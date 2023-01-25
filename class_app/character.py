from map import Point

class Character:

    NOT_ENOUGH_POWER_POINTS = "not_enough_power_points"

    def __init__(self, type, name, inventory = [], power_points = 10, can_teleport = False, position = Point(), token = "?"):
        
        self.type = type
        self.name = name
        self.inventory = inventory
        self.power_points = power_points
        self.can_teleport = can_teleport
        self.position = position
        self.token = token

    def run(self, direction, map):

        map.set_character_position(self, True)

        if direction == "north":
            self.position.y -= 1
        
        elif direction == "east":
            self.position.x += 1

        elif direction == "south":
            self.position.y += 1

        elif direction == "west":
            self.position.x -= 1

        if self.power_points >= 2:
            print(f"{self.name} is running {direction}.")
            self.power_points -= 2

            map.set_character_position(self)

            return True

        else:
            print(f"{self.name} only has {self.power_points} Power Points and cannot run.")
            return self.NOT_ENOUGH_POWER_POINTS

    def rest(self):

        if self.power_points < 10:
            print(f"{self.name} is resting.")
            self.power_points += 1
            return True
        
        else:
            print(f"{self.name} has {self.power_points} Power Points and does not need to rest.")
            return False

    def teleport(self, map):

        if self.power_points >= 4 and self.can_teleport:
            print(f"{self.name} is teleporting.")
            self.power_points -= 4
            return True

        elif self.power_points < 4:
            print (f"{self.name} only has {self.power_points} Power Points and cannot teleport.")
            return self.NOT_ENOUGH_POWER_POINTS

        else:
            print(f"{self.name} is not able to teleport.")
            return False
    
    def list_inventory(self):

        for item in self.inventory:
            print (item)