"""
Problem 1: Array Creation
"""
import numpy as np

# 1. Initialize an empty array with size 2x2
empty_arr = np.empty((2, 2))
print("1. Empty array (2x2):\n", empty_arr)

# 2. Initialize an all one array with size 4x2
ones_arr = np.ones((4, 2))
print("\n2. Ones array (4x2):\n", ones_arr)

# 3. Return a new array of given shape and type, filled with fill value
full_arr = np.full((3, 3), 7)  # filled with 7
print("\n3. Full array (3x3) filled with 7:\n", full_arr)

# 4. Return a new array of zeros with same shape and type as a given array
given_arr = np.array([[1, 2, 3], [4, 5, 6]])
zeros_like_arr = np.zeros_like(given_arr)
print("\n4. Zeros like given array:\n", zeros_like_arr)

# 5. Return a new array of ones with same shape and type as a given array
ones_like_arr = np.ones_like(given_arr)
print("\n5. Ones like given array:\n", ones_like_arr)

# 6. Convert an existing list to a numpy array
new_list = [1, 2, 3, 4]
np_arr = np.array(new_list)
print("\n6. List converted to numpy array:", np_arr)
print("   Type:", type(np_arr))
