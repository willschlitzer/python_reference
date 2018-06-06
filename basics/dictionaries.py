"""An explanation of dictionaries in Python"""

# A dictionary is a data format that contains keys and values
# keys must be immutable strings or tuples

my_dict = {(3, 2): 1, "a": 2}
print(my_dict)

# Specific keys can be called with an index name
print(my_dict["a"])

# Dictionaries can be called with a for loop
for key in my_dict:
    print(key)
