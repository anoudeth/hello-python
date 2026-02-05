# functions.py - Creating your own commands

print("=== Learning Functions ===")

# Simple function - no inputs needed
def say_hello():
    print("Hello from my function!")
    print("This is my first custom command!")

# Call (use) the function
print("1. Simple function:")
say_hello()

print("\n" + "="*30)

# Function with input (parameter)
def greet_person(name):
    print(f"Hello, {name}! Nice to meet you!")

print("2. Function with input:")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")

print("\n" + "="*30)

# Function that gives back a result (return)
def add_numbers(a, b):
    result = a + b
    return result

print("3. Function that returns a value:")
answer = add_numbers(5, 3)
print(f"5 + 3 = {answer}")

answer2 = add_numbers(10, 20)
print(f"10 + 20 = {answer2}")

print("\n" + "="*30)

# More useful functions
def calculate_area(length, width):
    area = length * width
    return area

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def make_sandwich(bread, filling):
    return f"{bread} sandwich with {filling}"

print("4. Practical functions:")

# Calculate room area
room_area = calculate_area(12, 10)
print(f"Room area: {room_area} square feet")

# Check if number is even
num = 7
if is_even(num):
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Make sandwich
my_sandwich = make_sandwich("wheat", "turkey")
print(f"I made a {my_sandwich}")

print("\n" + "="*30)

# Interactive function example
def simple_calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"
    else:
        return "Unknown operation!"

print("5. Interactive calculator function:")

# Get input from user
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
op = input("Enter operation (add, subtract, multiply, divide): ")

result = simple_calculator(first, second, op)
print(f"Result: {result}")

print("\n" + "="*30)

# Function that uses other functions
def describe_number(num):
    if is_even(num):
        even_odd = "even"
    else:
        even_odd = "odd"
    
    if num > 0:
        sign = "positive"
    elif num < 0:
        sign = "negative"
    else:
        sign = "zero"
    
    return f"{num} is a {sign} {even_odd} number"

print("6. Function using other functions:")
test_num = int(input("Enter a number to describe: "))
description = describe_number(test_num)
print(description)