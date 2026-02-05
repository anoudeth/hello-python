# function_exercises.py - Practice creating functions

print("=== Function Exercises ===")

# Exercise 1: Create a function that says your name
def my_intro():
    # TODO: Change this to your actual name
    print("My name is [Your Name]")
    print("I'm learning Python!")

print("1. Introduction function:")
my_intro()

print("\n" + "="*30)

# Exercise 2: Function that takes age and tells you something
def age_message(age):
    if age < 18:
        return f"You are {age} years old. You're still young!"
    else:
        return f"You are {age} years old. You're an adult!"

print("2. Age message function:")
user_age = int(input("Enter your age: "))
message = age_message(user_age)
print(message)

print("\n" + "="*30)

# Exercise 3: Temperature converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("3. Temperature converter:")
temp_c = float(input("Enter temperature in Celsius: "))
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f_input = float(input("Enter temperature in Fahrenheit: "))
temp_c_result = fahrenheit_to_celsius(temp_f_input)
print(f"{temp_f_input}°F = {temp_c_result:.1f}°C")

print("\n" + "="*30)

# Exercise 4: String functions
def reverse_text(text):
    return text[::-1]

def count_words(sentence):
    words = sentence.split()
    return len(words)

def make_title_case(text):
    return text.title()

print("4. Text functions:")
user_text = input("Enter some text: ")

reversed_text = reverse_text(user_text)
word_count = count_words(user_text)
title_text = make_title_case(user_text)

print(f"Original: {user_text}")
print(f"Reversed: {reversed_text}")
print(f"Word count: {word_count}")
print(f"Title case: {title_text}")

print("\n" + "="*30)

# Exercise 5: Simple game functions
def roll_dice():
    import random
    return random.randint(1, 6)

def play_dice_game():
    print("Let's play a dice game!")
    print("Roll two dice, if sum is 7 or 11, you win!")
    
    input("Press Enter to roll the dice...")
    
    dice1 = roll_dice()
    dice2 = roll_dice()
    total = dice1 + dice2
    
    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    print(f"Total: {total}")
    
    if total == 7 or total == 11:
        print("🎉 YOU WIN!")
    else:
        print("😐 You lose, try again!")

print("5. Dice game:")
play_dice_game()