num1 = 42  #variable declaration: number (integer) initialized
num2 = 2.3  #variable declaration: number (float/decimal) intialized
boolean = True  #variable declaration: boolean initialized
string = 'Hello World' #variable declaration: string initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #variable declaration: list initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #variable declaration: dictionary initialized
fruit = ('blueberry', 'strawberry', 'banana')  #variable declaration: tuple initialized
print(type(fruit))  #prints to console: type check 
print(pizza_toppings[1]) #print to console: list access value
pizza_toppings.append('Mushrooms')  #list add value 
print(person['name'])  #prints to console: list access value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue'  #dictionary add value 
print(fruit[2])  #prints to console: tuple access data

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#conditional if statement, evaluation, print to console, conditional else, print to console


if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#conditional if/elif/else statement, print to console 

    

for x in range(5):
    print(x)
#for loop starting at 0 going up until 5

    
for x in range(2,5):
    print(x)
#for loop starting at 2 going up until 5

    
for x in range(2,10,3):
    print(x)
x = 0
#for loop starting at 2 going up until 10 and increments by 3


while(x < 5):
    print(x)
    x += 1
#while loop, variable declaration, prints to console, increments x

    

pizza_toppings.pop()  #list delete end value
pizza_toppings.pop(1)  #list delete value at index


print(person) #prints to console entire dictionary 
person.pop('eye_color')  #dictionary delete value
print(person)  #prints to console entire dictionary



for topping in pizza_toppings:   #for loop through list
    if topping == 'Pepperoni':   #conditional if
        continue                #continues
    print('After 1st if statement') #print to console
    if topping == 'Olives':    #conditional if
        break    #ends the loop


    

def print_hello_ten_times():  #function declaration
    for num in range(10):   #for loop starting at 0 going up until 10
        print('Hello')   #prints to console


print_hello_ten_times()  #function call


def print_hello_x_times(x): #function declaration with parameter x
    for num in range(x):    #for loop up until given number (x)
        print('Hello')    #prints to console

print_hello_x_times(4)   #function call with argument 

def print_hello_x_or_ten_times(x = 10):  #function declaration with default parameter
    for num in range(x):   #for loop up until x
        print('Hello')   #prints to console

print_hello_x_or_ten_times()   #function call goes to 10
print_hello_x_or_ten_times(4)   #function call go to 4


"""
Bonus section
"""

# print(num3)  #print variable
# num3 = 72   #variable declaration: number (integer) initialized
# fruit[0] = 'cranberry'  #tuple change value
# print(person['favorite_team'])  #prints to console access value
# print(pizza_toppings[7])   #ERROR - there are not eight items in the pizza toppings list
#   print(boolean)   #prints to console 
# fruit.append('raspberry')  #tuple add value
# fruit.pop(1)  #tuple delete value
