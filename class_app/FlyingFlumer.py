from Character import Character
from map import Point

# inheritance
class FlyingFlumer(Character):

    def __init__(self, name, inventory = [], power_points=10, position=Point()):
        super(FlyingFlumer, self).__init__('FlyingFlumer', name, inventory, power_points, True, position, 'F')

    
    #override a method
    def run(self, direction, map):
        print("Flying Flumers can't run silly!")

    def fly(self, direction, map):

        map.set_character_position(self, True)

        if direction == 'north':
            self.position.y -=1

        elif direction == 'east':
            self.position.x += 1

        elif direction == 'south':
            self.position.y += 1

        elif direction == 'west':
            self.position.x -= 1

        if self.power_points >= 2:
            print( f'{self.name} is flying {direction}.')
            self.power_points -= 2

            map.set_character_position(self)

            return True