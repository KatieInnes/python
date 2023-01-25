class Pet:
    def __init__(self, name, type, tricks, noise, health = 0, energy = 0):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = health
        self.energy = energy

    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"{self.name}'s energy is {self.energy}.")
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s energy is {self.energy} and health is {self.health}.")
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"{self.name}'s health is {self.health}.")
        return self

    # noise() - prints out the pet's sound
    def sound(self):
        print(f"{self.name} says '{self.noise}'.")
        return self

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, Pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
    
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.sound()
        return self

# Pets
rusty = Pet("Rusty", "dog", "give a high five", "bark, bark, bark", health =  25, energy = 40)
nova = Pet("Nova", "cat", "play laser tag", "meow, meow")
furry = Pet("Furry", "gerbil", "spin its wheel very fast", "sniff, sniff", health = 30, energy = 100)

# Ninjas
lisa = Ninja("Lisa", "Congdon", "meatballs", "kibble", rusty)
wendy = Ninja("Wendy","McNaughton","catnip","tuna", nova)
amos = Ninja("Amos", "Goldbaum", "carrots", "fruit", furry)

wendy.walk().feed().bathe()

lisa.walk().feed().bathe()

amos.walk().feed().bathe()


    
    