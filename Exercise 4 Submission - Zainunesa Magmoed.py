#Question 1: Using a for loop with a list

# TODO: Create a list of fruits
Fruit = ['Apple','Banana','pear', 'orange','strawberry' ]
# TODO: Use a for loop to print each fruit in the list
for list in Fruit:
    print(list)

#-------------------------------------------------------------------------
#Question 2: Using a while loop for countdown

#TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count > 0:
    print(count)
    count -= 1
    

#--------------------------------------------------------------------------
#Question 3: Using a for loop with range()

#TODO: Use a for loop to print the first 10 square numbers
for square_number in range (1,10,2):
    print(square_number)

#-------------------------------------------------------------------------

#Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colors = ['Red', 'white', 'grey', 'blue', 'orange']
# TODO: Use a for loop to select and print 3 random colors from the list
random_selected_colors = random.sample(colors, 3)

for color in random_selected_colors:
    print(color)
#-------------------------------------------------------------------------
#Question 5: Creating and using a custom module

#TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations

print(math_operations.add(8, 2))
print(math_operations.subtract(8, 2))
print(math_operations.multiply(8, 2))
print(math_operations.divide(8, 2)) 

# TODO: Use a while loop to create a simple calculator

number1 = float(input("Number: "))
Operation = input("Enter an operation, either (+, -, *, /): ")
number2 = float(input("Number: "))

while number > 0:
    number1 = float(input("Number: "))
print(number1)


result = 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
    
print(result)