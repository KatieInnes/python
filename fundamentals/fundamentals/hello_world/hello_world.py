# 1. TASK: print "Hello World"
print("Hello", "World")


# 2. print "Hello Katie!" with the name in a variable
name = "Katie"
print("Hello", name,"!")	# with a comma
print("Hello "+ name + "!")	# with a +

# 3. print "Hello 25!" with the number in a variable
name = 25
print("Hello", 25, "!")	# with a comma
# print("Hello " + 25, "!")	# with a +	-- this one should give us an error!
print("Hello " + str(25) + "!")

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "udon noodles"
fave_food2 = "chocolate cake"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string
print("I love to eat %s and %s."% (fave_food1, fave_food2))  #with % formating
