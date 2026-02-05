# loops.py - Making Python repeat things

print("=== Learning Loops ===")

# 1. FOR LOOP - Repeat a specific number of times
print("1. Basic for loop - count to 5:")
for i in range(5):
    print(f"Count: {i}")

print("\n" + "="*30)

# 2. FOR LOOP with different ranges
print("2. Different counting:")

print("Count 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

print("Count by 2s from 0 to 10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

print("Count backwards from 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("\n" + "="*30)

# 3. FOR LOOP with lists
print("3. Loop through a list:")
fruits = ["apple", "banana", "orange", "grape"]

print("My fruits:")
for fruit in fruits:
    print(f"- I like {fruit}")

print("Numbered list:")
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")

print("\n" + "="*30)

# 4. WHILE LOOP - Repeat while condition is true
print("4. While loop - guess the number:")

import random
secret = random.randint(1, 10)
guess = 0
attempts = 0

print("I'm thinking of a number between 1-10")
while guess != secret:
    guess = int(input("Your guess: "))
    attempts += 1
    
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"🎉 Correct! You got it in {attempts} attempts!")

print("\n" + "="*30)

# 5. Practical loop examples
print("5. Practical uses:")

# Sum numbers
print("Adding numbers 1 to 100:")
total = 0
for i in range(1, 101):
    total += i
print(f"Sum = {total}")

# Create a multiplication table
print("\nMultiplication table for 5:")
for i in range(1, 11):
    result = 5 * i
    print(f"5 × {i} = {result}")

print("\n" + "="*30)

# 6. Interactive examples
print("6. Interactive loops:")

# Collect user input
shopping_list = []
print("Enter items for shopping list (type 'done' to finish):")

while True:
    item = input("Item: ")
    if item.lower() == 'done':
        break
    shopping_list.append(item)

print("\nYour shopping list:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")

print("\n" + "="*30)

# 7. Loop with conditions
print("7. Finding even numbers:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("All numbers:")
for num in numbers:
    print(num, end=" ")
print()

print("Even numbers only:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
print()

print("Numbers greater than 5:")
for num in numbers:
    if num > 5:
        print(num, end=" ")
print()

print("\n" + "="*30)

# 8. Nested loops (loops inside loops)
print("8. Pattern with nested loops:")

print("Simple pattern:")
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

print("\nNumber pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()