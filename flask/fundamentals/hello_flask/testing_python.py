##import random
##
##print('Welcome to Python!')
##
##print('This is a loop printing 5 times')
##for x in range(1, 6):
##    print(f'x is: {x}')
##
##weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
##day = random.choice(weekdays)
##
##print(f'Today is: {day}')
##
##if day == 'Monday':
##    print('It will be a long week!')
##elif(day == 'Friday'):
##    print('Woohoo, time for the weekend!')
##else:
##    print('Not quite there yet.')


##pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  
##person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} 
##print(pizza_toppings[1])
##pizza_toppings.append('Mushrooms')
##
##for topping in pizza_toppings:
##    if topping == 'Pepperoni':
##        continue
##    print('After 1st if statement')
##    if topping == 'Olives':
##        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
