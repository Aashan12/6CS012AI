"""
Task 2: Element-wise Multiplication - Python Lists vs NumPy
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
result_list = [list_a[i] * list_b[i] for i in range(size)]
end = time.time()
list_time = end - start
print(f"Python List Multiplication Time: {list_time:.5f} seconds")

# --- NumPy Array ---
start = time.time()
result_np = np_a * np_b
end = time.time()
np_time = end - start
print(f"NumPy Array Multiplication Time: {np_time:.5f} seconds")

# --- Comparison ---
print(f"\nNumPy is ~{list_time / np_time:.1f}x faster than Python lists for element-wise multiplication.")
