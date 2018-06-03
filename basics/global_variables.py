"""An explanation of global and local variables"""

# Variables defined outside of functions are considered global
# Global variables can be used in other functions

num = 3

def print_global():
    # Print global variable
    print(num)

# Call function
print_global()

# Variables can be defined in functions as global
def make_global():
    # Creates a global variable inside a function
    global num2
    num2 = 10

make_global()
# Calls global variable outside of the function that defined it
print(num2)