"""Demonstrates the basic applications for statistical analysis with numpy"""
# numpy a not a default module and needs to be installed
# A common convention is to rename numpy to 'np' upon import
import numpy as np


x = [2,3,4,5,6,3,2,3,45,3]
# The array() function converts a list of data into an array
# An array can be manipulated mathmatically
x_array = np.array(x)
print('Data')
print(x_array)
print('Mean', x_array.mean())
print('Standard deviation', x_array.std())