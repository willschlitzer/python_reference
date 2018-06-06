"""And explanation of lists in Python"""

# A list is an ordered set of data

# Lists are defined with the square brackets: []
# Every entry in a list is separated by a comma

my_list = [1, 2, 3, 4, 5]

# Every entry in a list is indexed, beginning at 0
# The desired index of a list is indicated after the list name with square brackets
print("Index")
print(my_list[3])
# Inidices also work in reverse
# Returns the final item
print("Reverse index")
print(my_list[-1])

# Data types in lists do not have to be uniform
mix_list = [1, "a", 3.0, True]
print("Mix list")
print(mix_list)

# Data from lists can be sliced out with the indices
# The indices of the start (inclusive) and end (non-inclusive) are given
print("Slicing list")
print(my_list[2:4])
# Leaving indices blank indicates either the beginning or the end
print("Empty indices")
print(my_list[:3])
print(my_list[1:])
# An additional colon can be given with the steps (in this case 2) for slicing
print("Steps in a slice")
print(my_list[::2])
