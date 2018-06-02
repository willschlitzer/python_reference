"""An explanation of importing modules"""

# import statements can be used to import
# functions, classes, and variables from other files

# import can be used on built-in and installed modules
import math
import pandas

# if the entire module is called, specific functions
# and variables must be prefaced with module name
print(math.tau)

# specific functions and variables can be imported
from math import pi
print(pi)
# All functions/variables can be imported
# This is not common practice
from math import *
print(tau)

# imported functions and programs can be renamed
import numpy as np
