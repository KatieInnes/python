from character import Character
from map import Map, Point

characters = [
    Character("Fuzzball", "Fred", ["food", "fireball", "shield"], can_teleport = True, position = Point(1,2), token = "F"),
    Character("FurOFury", "Firora", [], position = Point(3,4), token = "O"),
    Character("BeatleBop", "Betty", ["food", "sword", "silly stones"], can_teleport = True, position = Point(5,6), token = "B")
]

is_active = True
map = Map(characters)

def get_character(character_name):

    for character in characters:
        if character.name == character_name:
            return character

    return None

def do_action(action, direction, character):

    if action == "run":

        character.run(direction, map)

    elif action == "rest":

        character.rest()

    elif action == "teleport":

        character.teleport()

    elif action == "inventory":
        
        character.list_inventory()

    else:
        print("Invalid action")

while is_active:

    line_input = input("Command? ").strip()

    if line_input == "":
        continue

    line_parts = (line_input + "  ").split(" ")

    command = line_parts[0]
    action = line_parts[1]
    extra = line_parts[2]

    if command == "quit":
        is_active = False
        continue

    elif command == "view-map":
        map.view()
        continue

    elif command == "view-characters":
        for character in characters:
            print(f"{character.token} : {character.name}")
        continue

    character = get_character(command)

    if character is None:
        print("Invalid character")
        continue

    do_action(action, extra, character)
