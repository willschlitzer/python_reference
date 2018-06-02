"""An explanation of the main data types used in Python"""

# There are 3 main data types in Python: strings, integers, and floats
# There are also Boolean statements

# A string can include any character
# A string's data is cannot be changed
# Numbers do not have their value when they are in strings

# The type() function returns the type of data that was inputted to this
# The print() function prints what type() returns
# In this class, it is class 'str' for string
print(type('Hello'))

# An integer is a whole number
# It does have a number value
# When added, subtracted, or multiplied with another integer, the result is also an integer
# Divison, even when resulting in a whole number, returns a float
print(type(3))
print(type(3+3))
printg(type(5-3))
print(type(5*3))
print(type(6/2))

# A float is any number including decimals
# When uses with an integer, the result is an float
# Even when a whole number, the addition of a decimal point makes a number a float
print(type(3.5))
print(type(3.0))
print(type(5 + 3.0))

# A Boolean statement can be evaluated as a True/False
# It is not only the literal True/False statement, but equations that can be evaluated as True/False
print(type(True))
print(type(3 == 5))