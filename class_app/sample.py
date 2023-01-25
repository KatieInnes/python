# day = 1
# date = 1
# year = 1970

# # typecasting
# year_end = int(str(year)[-2:]) # slicing - using a negative number will slice from the end
# year_end_mod = year % 100

# print(year_end)



""""""""

# class SomeClass:

#     class_level_attribute = None

#     def __init__(self):
#         self.instance_level_attribute = None
        
# SomeClass.class_level_attribute

# some_thing = SomeClass()
# some_thing.instance_level_attribute


""""""""
is_active = True

while is_active:

    line_input = input("Command? ").strip()

    print(line_input)

    line_parts = (line_input + "  ").split(" ")

    command = line_parts[0]
    extra_1 = line_parts[1]
    extra_2 = line_parts[2]

    if command == "quit":
        is_active = False

    elif command == "walk":

            print(f"I am walking {extra_1} {extra_1} sapces.")

    elif command == "cast-spell":

        print(f"I am casting an {extra_1} spell with {extra_2} power.")

    else:
        print("Invalid Command")
