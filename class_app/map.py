class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


class Map:

    def __init__(self, characters = None):
        self.reset()
        if characters:
            self.add_characters(characters)

    def add_characters(self, characters):

        for character in characters:
            self.set_character_position(character)

    def reset(self):
        
        self.grid = [ #y
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ], #x
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ],
            ['.', '.', '.' ,'.', '.', '.', '.' ,'.', '.', '.' ]
        ]

    def set_character_position(self, character, clear = False):
        self.grid[character.position.y][character.position.x] = '.' if clear else character.token

    def get_grid_square(self, point):
        return self.grid[point.y][point.x]

    def view(self):
        
        top_row = " "
        for x in range(10): # 0-index end 9
            top_row += f' {x}'
        print ( top_row )

        for index, row in enumerate(self.grid):
            print( f'{str(index)} {" ".join(row)}' )
