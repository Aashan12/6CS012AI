"""
Task 4: Matrix Multiplication - Python Lists vs NumPy
(1000x1000 matrices)
"""
import numpy as np
import time

size = 1000

# Create 1000x1000 matrices as lists and numpy arrays
list_A = [[1 for _ in range(size)] for _ in range(size)]
list_B = [[1 for _ in range(size)] for _ in range(size)]
np_A = np.ones((size, size))
np_B = np.ones((size, size))

# --- Python List ---
print("Running Python list matrix multiplication (this may take a while)...")
start = time.time()
result_list = [[sum(list_A[i][k] * list_B[k][j] for k in range(size))
                for j in range(size)]
               for i in range(size)]
end = time.time()
list_time = end - start
print(f"Python List Matrix Multiplication Time: {list_time:.5f} seconds")

# --- NumPy Array ---
start = time.time()
result_np = np.dot(np_A, np_B)
end = time.time()
np_time = end - start
print(f"NumPy Array Matrix Multiplication Time: {np_time:.5f} seconds")

# --- Comparison ---
print(f"\nNumPy is ~{list_time / np_time:.1f}x faster than Python lists for matrix multiplication.")
