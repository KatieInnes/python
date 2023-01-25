class Character:
    
    NOT_ENOUGH_POWER_POINTS = "not_enough_power_points"  #CONST Constant - it's in all caps, therefore a constant that should not be changed.

    #constructor
    def __init__(self, type, name, inventory = [], power_points = 10, can_teleport = False):
        self.type = type
        self.name = name
        self.inventory = inventory
        self.power_points = power_points
        self.can_teleport = can_teleport

    def run(self):

        if self.power_points >= 2:
            print(f"{self.name} is running.")
            self.power_points -= 2
            return True

        else:
            print(f"{name} only has {power_points} Power Points and cannot run.")
            return Character.NOT_ENOUGH_POWER_POINTS

    def rest(self):
        if self.power_points < 10:
            while self.power_points < 10:
                print(f"{self.name} is resting.")
                self.power_points +=1
            return True

        else:
            print(f"{self.name} has {self.power_points}Power Points and does not need to rest.")
            return False

    def teleport(self):
        if power_points >= 4 and can_teleport:
            print(f"{name} is teleporting.")
            power_points -= 4
            return True

        elif power_points < 4:
            print(f"{name} only has {power_points} Power Points and cannot teleport.")
            return self.NOT_ENOUGH_POWER_POINTS

        else:
            print(f"{name} is not able to teleport.")
            return False

    def list_inventory(self):

        for item in self.inventory:
            print(item)
