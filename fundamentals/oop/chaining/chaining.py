class User:

    def __init__(self, first_name, last_name, email, age, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

# display_info(self) - Have this method print all of the users' details on separate lines.
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.

    def enroll(self):
        # Bonus for myself: If the user is younger than 18, disallow them from joining and print "'first_name' is too young to join rewards program."
        if self.age <18:
            print(f"{self.first_name} is too young to join the rewards program.")
        elif self.is_rewards_member == True:
            print(f"{self.first_name} is already a member.")
        else:    
            self.is_rewards_member = True
            self.gold_card_points = self.gold_card_points + 200
        return self

# spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points = self.gold_card_points - amount
            print(self.gold_card_points)
        else:
            print(f"{self.first_name} has {self.gold_card_points} gold card points and cannot spend that amount.")
        return self


katie = User("Katie", "Innes", "katharine.innes@gmail.com", 38)
katie.display_info().enroll().spend_points(50).display_info().enroll()

leslie = User("Leslie", "Thomas", "lthomas@yahoo.com", 69)
maddie = User("Maddie", "Thomas", "tarotgirl@gmail.com", 27)
brynjar = User("Brynjar", "Baldvinsson", "b.baldvinsson@s.sfusd.edu", 8)

leslie.enroll().spend_points(80).display_info()

maddie.display_info().spend_points(40)

brynjar.display_info().enroll()
