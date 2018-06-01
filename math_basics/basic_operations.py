"""A demonstration of basic math operations in Python"""
# Does not include the math module

# Addition
print('Addition')
print(3+3)

# Subtraction
print('Subtraction')
print(6-3)

# Multiplication
print('Multiplication')
print(3*4)

# Division
print('Division')
print(5/3.0)

# Exponents
print('Exponents')
# The double asterisk (**) is used instead of the carat (^)
print(3**2)

# Order of operations is automatically implemented
# Please Excuse My Dear Aunt Sarah
# Parenthesis Exponents Multiplcation Division Addition Subtraction
print('Order of operations')
print('Without parenthesis')
print(3+6/2**2)
print('With parenthesis')
print(((3+6)/2)**2)

# Python has a built in rounding function
x= 3.1415926535
print('Unrounded', x)
# round() function takes 2 arguments: the float, and the number of digits after the decimal place
print('Rounded to 4 decimals', round(x, 4))