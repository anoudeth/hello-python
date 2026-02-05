# conditions.py - Making decisions in Python

print("=== Simple Decision Making ===")

# Age checker
age = int(input("How old are you? "))

if age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 60:
    print("You're an adult!")
else:
    print("You're a senior!")

print("\n=== Simple Game ===")

# Number guessing game
import random

secret_number = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10...")

guess = int(input("What's your guess? "))

if guess == secret_number:
    print("🎉 Wow! You got it!")
elif guess < secret_number:
    print("Too low! The number was", secret_number)
else:
    print("Too high! The number was", secret_number)

print("\n=== Grade Calculator ===")

# Simple grade calculator
score = int(input("Enter your test score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your score: {score}")
print(f"Your grade: {grade}")

if grade in ["A", "B"]:
    print("Great job! 🌟")
elif grade == "C":
    print("Not bad, but you can do better!")
else:
    print("Keep studying! 📚")