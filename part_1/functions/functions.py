# Defining a function
def greet_user(username):
    """Display a simple greeting.""" # Function docstring
    print(f"Hello, {username.title()}!")
    
# Keyword arguments
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Returning values
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Making an argument optional
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

# Using a function with a list
def greet_users(names):
    """Print a greeting to each user in the list."""
    for name in names:
        print(f"Hello, {name.title()}!")

# Using a function with arbitrary arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Using a function with arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Modifying a list in a function
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

# Showing completed models
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# PReventing a function from modifying a list
def make_great(magicians):
    """Add 'the Great' to each magician's name."""
    for i in range(len(magicians)):
        magicians[i] = f"The Great {magicians[i]}"
        
# Storing functions in a module
# This file can be saved as functions.py and imported in other files.