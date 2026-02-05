# lists.py - Working with lists

print("=== Working with Lists ===")

# Create a list of favorite foods
foods = ["pizza", "burger", "sushi", "ice cream"]

print("My favorite foods:")
for food in foods:
    print(f"- {food}")

print(f"\nI have {len(foods)} favorite foods")
print(f"My first favorite is: {foods[0]}")
print(f"My last favorite is: {foods[-1]}")

# Add new food
foods.append("chocolate")
print(f"\nAfter adding chocolate: {foods}")

print("\n=== Numbers List ===")

# List of numbers
numbers = [1, 5, 10, 3, 8]
print(f"Numbers: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Largest: {max(numbers)}")
print(f"Smallest: {min(numbers)}")

print("\n=== Interactive List ===")

# Let user build their own list
my_list = []
print("Enter 3 things you like (press Enter after each):")

for i in range(3):
    item = input(f"Item {i+1}: ")
    my_list.append(item)

print(f"\nYour list: {my_list}")
print("Here are your items:")
for i, item in enumerate(my_list, 1):
    print(f"{i}. {item}")