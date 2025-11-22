# A simple dictionary to demonstrate dictionary operations in Python
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])
print(person.get("age"))

# Modifying values
person["age"] = 31
print(person)

# Adding new key-value pairs
person["profession"] = "Engineer"
print(person)

# Removing key-value pairs
del person["city"]
print(person)

# Looping through the dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension to create a dictionary of squares
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)

# Merging two dictionaries
additional_info = {"hobby": "painting", "country": "USA"}
person.update(additional_info)
print(person)

# Checking for existence of a key
if "name" in person:
    print("Name is present in the dictionary.")
    
# Getting all keys and values
print(person.keys())
print(person.values())
print(person.items())

# Nested dictionaries
students = {
    "student1": {"name": "Bob", "age": 22},
    "student2": {"name": "Charlie", "age": 23}
}

for student_id, student_info in students.items():
    print(f"{student_id}:")
    for key, value in student_info.items():
        print(f"  {key}: {value}")

# Using the pop method to remove a key and return its value
age = person.pop("age")
print(f"Removed age: {age}")
print(person)

# Using the popitem method to remove and return the last inserted key-value pair
last_item = person.popitem()
print(f"Removed item: {last_item}")
print(person)

# Copying a dictionary
person_copy = person.copy()
print(f"Copied dictionary: {person_copy}")

# Clearing a dictionary
person.clear()
print(f"Cleared dictionary: {person}")

# Demonstrating the use of defaultdict from collections module
from collections import defaultdict
default_dict = defaultdict(int)
default_dict["a"] += 1
default_dict["b"] += 2
print(default_dict)