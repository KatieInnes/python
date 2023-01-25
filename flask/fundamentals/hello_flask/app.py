from character import Character   #import statement, tells the file to import the file "character.py" and from that the methods in the class "Character"

some_character = Character("Fuzzball", "Fred" ["food", "fireball", "shield"], 5)

characters = [ 
    Character("Fuzzball", "Fred", ["food", "fireball","shield"], 5)
    Character("BeatleBop", "Betty", ["food", "sword", "silly stones"], 1, True)
]

is_active = True

def get_character(character_name):

    for character in characters:
        if character.name == character_name: 
            return character

    return None

def do_action(action, character, extra):

    if action == 'run':

        if character.run() == Character.NOT_ENOUGH_POWER_POINTS:
            character.rest()

    elif action == 'rest':
        
        character.rest()

    elif action == 'teleport':
        
        character.teleport()

    elif action == 'inventory':

        character.list_inventory()

    elif action == inventory.append(extra)

    else:
        print ("Invalid action")

def reset_characters():
    for character in characters:
        character['power_points'] = 10

def update_character_inventory(character, item):
    character['inventory'].append(item)

while is_active: 

    line_input = input('command? ').strip() 

    if line_input == "": 
        continue

    line_parts = (line_input + "  ").split(" ")

    command = line_parts[0]
    action = line_parts[1]
    extra = line_parts[2]

    if command == 'quit':
        is_active = False
        continue

    character = get_character(command)

    if character is None:
        print("invalid character")
        continue

    do_action(action, character)
    