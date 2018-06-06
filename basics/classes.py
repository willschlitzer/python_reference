"""An explanation of classes"""

# Classes create an instance and store it in a variable
# Data can be stored and changed within the variable


class Friends:
    """A class stores data and runs functions"""

    def __init__(self, first, last, age):
        """The init function runs upon the instance being called"""
        self.age = age
        self.first = str.title(first)
        self.last = str.title(last)

    def phone_number(self, number):
        """Additional functions can be called in a class"""
        # Subsequent variables can be assigned
        self.number = number


# Calls the init function in the class
will = Friends("will", "schlitzer", 28)
# Demonstrates the variable is stored from the class
print(will.first)
# Call a subsequent function to assign a new variable
will.phone_number("508-742-8232")
print(will.number)
