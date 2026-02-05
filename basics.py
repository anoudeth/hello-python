# basics.py - Simple Python concepts

print("=== Python Basics ===")

# Variables - storing information
name = "John"
age = 25
height = 5.8
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is student: {is_student}")

print("\n=== Simple Math ===")

# Basic math operations
a = 10
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")

print("\n=== User Input ===")

# Getting input from user
user_name = input("What's your name? ")
print(f"Nice to meet you, {user_name}!")

# Simple calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2
print(f"{num1} + {num2} = {result}")