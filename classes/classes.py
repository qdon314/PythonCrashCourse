# Creating and using a class
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
        
# Creating an instance of the Dog class
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling methods on the Dog instance
my_dog.sit()
my_dog.roll_over()

# Inheritance example
class Labrador(Dog):
    """Represent a Labrador, a specific kind of dog."""

    def __init__(self, name, age, color):
        """Initialize attributes of the parent class."""
        super().__init__(name, age)
        self.color = color

    def fetch(self, item):
        """Simulate fetching an item."""
        print(f"{self.name} is fetching the {item}!")
                
    # Over4erriding a method
    def sit(self): 
        """Simulate a Labrador sitting in a specific way."""
        print(f"{self.name} the Labrador is sitting obediently.")