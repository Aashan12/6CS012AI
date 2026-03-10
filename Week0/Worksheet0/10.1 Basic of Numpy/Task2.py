"""
Problem 2: Array Manipulation - Numerical Ranges and Array Indexing
"""
import numpy as np

# 1. Create an array with values ranging from 10 to 49
arr1 = np.arange(10, 50)
print("1. Array from 10 to 49:\n", arr1)

# 2. Create a 3x3 matrix with values ranging from 0 to 8
arr2 = np.arange(0, 9).reshape(3, 3)
print("\n2. 3x3 matrix (0 to 8):\n", arr2)

# 3. Create a 3x3 identity matrix
identity = np.eye(3)
print("\n3. 3x3 Identity matrix:\n", identity)

# 4. Create a random array of size 30 and find the mean
rand_arr = np.random.random(30)
print("\n4. Random array of size 30:\n", rand_arr)
print("   Mean:", rand_arr.mean())

# 5. Create a 10x10 array with random values, find min and max
rand_10x10 = np.random.random((10, 10))
print("\n5. 10x10 random array:")
print("   Min:", rand_10x10.min())
print("   Max:", rand_10x10.max())

# 6. Create a zero array of size 10 and replace 5th element with 1
zero_arr = np.zeros(10)
zero_arr[4] = 1  # 5th element (index 4)
print("\n6. Zero array with 5th element = 1:", zero_arr)

# 7. Reverse an array
arr = np.array([1, 2, 0, 0, 4, 0])
reversed_arr = arr[::-1]
print("\n7. Original:", arr)
print("   Reversed:", reversed_arr)

# 8. Create a 2D array with 1 on border and 0 inside
border_arr = np.ones((5, 5))
border_arr[1:-1, 1:-1] = 0
print("\n8. 2D array with 1 on border, 0 inside:\n", border_arr)

# 9. Create an 8x8 checkerboard pattern
checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[::2, 1::2] = 1   # even rows, odd columns
checkerboard[1::2, ::2] = 1   # odd rows, even columns
print("\n9. 8x8 Checkerboard:\n", checkerboard)
