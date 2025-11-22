bycicles = ["trek", "redline", "giant"]
print(bycicles)
print(bycicles[0])

# Accessing the last element
print(bycicles[-1])

# Modifying elements
bycicles[0] = "ducati"
print(bycicles)

# Adding elements
bycicles.append("harley")
print(bycicles)

# Inserting elements at a specific position
bycicles.insert(1, "yamaha")
print(bycicles)

# Removing elements
del bycicles[2]
print(bycicles)

popped_bicycle = bycicles.pop()
print(bycicles)
print(f"Popped bicycle: {popped_bicycle}")

# Removing by value
bycicles.remove("redline")
print(bycicles)

# Sorting the list permanently
bycicles.sort()
print(bycicles)

# Sorting the list temporarily
print(sorted(bycicles))
print(bycicles)

# Reversing the list
bycicles.reverse()
print(bycicles)

# Finding the length of the list
print(len(bycicles))

# Looping through the list
for bicycle in bycicles:
    print(bicycle.title())

# Creating a list of numbers
squares = [value**2 for value in range(1, 11)]
print(squares)

# Simple statistics
print(f"Min: {min(squares)}")
print(f"Max: {max(squares)}")
print(f"Sum: {sum(squares)}")
# List comprehension to create a list of even numbers
even_numbers = [value for value in range(1, 21) if value % 2 == 0]
print(even_numbers)

# List comprehension to create a list of odd numbers
odd_numbers = [value for value in range(1, 21) if value % 2 != 0]
print(odd_numbers)

# List comprehension to create a list of multiples of 3
multiples_of_3 = [value for value in range(1, 31) if value % 3 == 0]
print(multiples_of_3)

# Slicing a list
print(bycicles[0:2])
print(bycicles[1:3])
print(bycicles[:2])
print(bycicles[2:])

# Looping through a slice
for bicycle in bycicles[:2]:
    print(bicycle.title())

# Copying a list
my_bicycles = bycicles[:]
print(my_bicycles)

# Defining a tuple
dimensions = (1920, 1080)
print(dimensions[0])
print(dimensions[1])

# Looping through a tuple
for dimension in dimensions:
    print(dimension)
    
# Redefining a tuple
dimensions = (2560, 1440)
print(dimensions[0])
print(dimensions[1])

# Tuple unpacking
width, height = dimensions
print(f"Width: {width}, Height: {height}")

# Using a while loop with lists and dictionaries
numbers = [1, 2, 3, 4, 5]
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1

person = {"name": "Alice", "age": 30, "city": "New York"}
keys = list(person.keys())
index = 0
while index < len(keys):
    key = keys[index]
    print(f"{key}: {person[key]}")
    index += 1

