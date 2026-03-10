"""
Task 3: Dot Product - Python Lists vs NumPy
"""
import numpy as np
import time

size = 1_000_000

list_a = list(range(size))
list_b = list(range(size))
np_a = np.arange(size)
np_b = np.arange(size)

# --- Python List ---
start = time.time()
dot_list = sum(list_a[i] * list_b[i] for i in range(size))
end = time.time()
list_time = end - start
print(f"Python List Dot Product Time: {list_time:.5f} seconds")
print(f"  Result: {dot_list}")

# --- NumPy Array ---
start = time.time()
dot_np = np.dot(np_a, np_b)
end = time.time()
np_time = end - start
print(f"NumPy Array Dot Product Time: {np_time:.5f} seconds")
print(f"  Result: {dot_np}")

# --- Comparison ---
print(f"\nNumPy is ~{list_time / np_time:.1f}x faster than Python lists for dot product.")
