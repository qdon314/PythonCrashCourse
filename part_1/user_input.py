# How the input function works in Python
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

age = input("Enter your age: ")
print(f"You are {age} years old.")

favorite_color = input("Enter your favorite color: ")
print(f"Your favorite color is {favorite_color}.")

# Getting numerical input
height = input("Enter your height in cm: ")
height = float(height)  # Converting string input to float
print(f"You are {height} cm tall.")

