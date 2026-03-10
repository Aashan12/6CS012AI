"""
Problem 3: Array Operations
"""
import numpy as np

x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])

# 1. Add the two arrays
print("1. x + y:\n", x + y)
print("   v + w:", v + w)

# 2. Subtract the two arrays
print("\n2. x - y:\n", x - y)
print("   v - w:", v - w)

# 3. Multiply the array with any integer
print("\n3. x * 3:\n", x * 3)
print("   v * 5:", v * 5)

# 4. Find the square of each element
print("\n4. x squared:\n", np.square(x))
print("   v squared:", np.square(v))

# 5. Dot products
print("\n5. Dot products:")
print("   v . w =", np.dot(v, w))
print("   x . v =\n", np.dot(x, v))
print("   x . y =\n", np.dot(x, y))

# 6. Concatenate x and y along row, v and w along column
print("\n6. Concatenate x and y along rows (vstack):\n", np.vstack((x, y)))
print("   Concatenate v and w along column:\n", np.column_stack((v, w)))

# 7. Concatenate x and v - this will cause an error
print("\n7. Attempting to concatenate x and v:")
try:
    result = np.concatenate((x, v))
    print(result)
except ValueError as e:
    print(f"   Error: {e}")
    print("   Reason: x is 2D (shape 2x2) and v is 1D (shape 2,).")
    print("   They have different number of dimensions, so concatenation fails.")
