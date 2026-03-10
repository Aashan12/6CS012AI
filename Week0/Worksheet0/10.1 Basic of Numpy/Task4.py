"""
Problem 4: Matrix Operations
"""
import numpy as np

A = np.array([[3, 4], [7, 8]])
B = np.array([[5, 3], [2, 1]])

# ---- Part 1: Prove A * A^-1 = I ----
A_inv = np.linalg.inv(A)
result = np.dot(A, A_inv)
print("1. Prove A * A^-1 = I")
print("   A:\n", A)
print("   A^-1:\n", A_inv)
print("   A * A^-1:\n", np.round(result))
print("   Is identity?", np.allclose(result, np.eye(2)))

# ---- Part 2: Prove AB != BA ----
AB = np.dot(A, B)
BA = np.dot(B, A)
print("\n2. Prove AB != BA")
print("   AB:\n", AB)
print("   BA:\n", BA)
print("   AB == BA?", np.array_equal(AB, BA))

# ---- Part 3: Prove (AB)^T = B^T * A^T ----
AB_T = AB.T
BT_AT = np.dot(B.T, A.T)
print("\n3. Prove (AB)^T = B^T * A^T")
print("   (AB)^T:\n", AB_T)
print("   B^T * A^T:\n", BT_AT)
print("   Equal?", np.array_equal(AB_T, BT_AT))

# ---- Part 4: Solve system of linear equations ----
# 2x - 3y + z  = -1
#  x -  y + 2z = -3
# 3x +  y -  z =  9
print("\n4. Solve system of linear equations:")
print("   2x - 3y + z  = -1")
print("    x -  y + 2z = -3")
print("   3x +  y -  z =  9")

coeff = np.array([[2, -3, 1],
                   [1, -1, 2],
                   [3,  1, -1]])
b = np.array([-1, -3, 9])

# Using inverse method: X = A^-1 * B
coeff_inv = np.linalg.inv(coeff)
solution = np.dot(coeff_inv, b)
print("\n   Using inverse method (A^-1 * B):")
print(f"   x = {solution[0]:.4f}, y = {solution[1]:.4f}, z = {solution[2]:.4f}")

# Using np.linalg.solve
solution2 = np.linalg.solve(coeff, b)
print("\n   Using np.linalg.solve:")
print(f"   x = {solution2[0]:.4f}, y = {solution2[1]:.4f}, z = {solution2[2]:.4f}")
