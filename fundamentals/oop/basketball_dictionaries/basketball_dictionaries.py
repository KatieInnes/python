#Set up a new file and add the Player class with the given constructor

# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

#1. Challenge 1: Update the constructor to accept a dictionary (player) as an argument and set the attributes using the dictionary.
joel = {"name": "Joel Embiid", "age": 32, "position": "Power Foward", "team": "Philidelphia 76ers"}

class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

player_joel = Player(joel)
print(player_joel)
print(player_joel.team)


#2. Challenge 2: Create 3 instances of the Player class using the given dictionaries.

damian = {"name": "Damian Lillard", "age": 33, "position": "Point Guard", "team": "Portland Trailblazers"}
jason = {"name": "Jason Tatum", "age": 24, "position": "small forward", "team": "Boston Celtics"}
steph = {"name": "Stephen Curry", "age": 34, "position": "Point Guard", "team": "Golden State Warriors"}

player_damian = Player(damian)
player_jason = Player(jason)
player_steph = Player(steph)


#3. Challenge 3: Populate a new list with Player instances from the list of players. Write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

players = [
    {"name": "Kevin Durant", "age": 34, "position": "small forward", "team": "Brooklyn Nets"},
    {"name": "Jason Tatum", "age": 24, "position": "small forward", "team": "Boston Celtics"},
    {"name": "Stephen Curry", "age": 34, "position": "Point Guard", "team": "Golden State Warriors"},
    {"name": "Damian Lillard", "age": 33, "position": "Point Guard", "team": "Portland Trailblazers"},
    {"name": "Joel Embiid", "age": 32, "position": "Power Foward", "team": "Philidelphia 76ers"},
    {"name": "", "age": 16, "position": "P", "team": "en"}
]

# ... (class definition and large list of players here)
new_team = []
# # Write your for loop here to populate the new_team variable with Player objects.
for players_dictionary in players:
    player = Player(players_dictionary)
    new_team.append(player)
print(new_team)
