import numpy as np
matrix = np.random.randint(0, 1000, (10, 10))
flat_indices = np.argpartition(matrix.flatten(), -3)[-3:]
sorted_top_indices = flat_indices[np.argsort(-matrix.flatten()[flat_indices])]
top_indices = np.unravel_index(sorted_top_indices, matrix.shape)

print("Matrix:\n", matrix)
print("Top 3 maximum values and their indices:")
for i in range(3):
    r, c = top_indices[0][i], top_indices[1][i]
    print(f"Value: {matrix[r, c]}, Index: ({r}, {c})")


A = np.array([[2, -1, 3],
              [1, 1, 1],
              [3, -1, -2]])

B = np.array([9, 6, -1])
x = np.linalg.solve(A, B)
print("Solution (x, y, z):", x)


M = np.random.rand(8, 8)
eigenvalues, eigenvectors = np.linalg.eig(M)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)


import time
large_matrix = np.random.rand(1000, 1000)

start_time = time.time()
matrix_sum = np.sum(large_matrix)
end_time = time.time()

print("Sum of elements:", matrix_sum)
print("Time taken (seconds):", end_time - start_time)


A = np.random.rand(500, 500)
B = np.random.rand(500, 500)

start_manual = time.time()
C_manual = np.zeros((500, 500))
for i in range(500):
    for j in range(500):
        C_manual[i, j] = np.sum(A[i, :] * B[:, j])
end_manual = time.time()
manual_time = end_manual - start_manual

start_dot = time.time()
C_dot = np.dot(A, B)
end_dot = time.time()
dot_time = end_dot - start_dot

print("Manual multiplication time (seconds):", manual_time)
print("NumPy dot multiplication time (seconds):", dot_time)
