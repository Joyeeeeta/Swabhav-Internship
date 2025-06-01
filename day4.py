import numpy as np
mat = np.random.randint(0, 10, (4, 4))
np.fill_diagonal(mat, 7)
print(mat)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
product = np.multiply(a, b)
print(product)

mat = np.random.rand(6, 6)
mean = np.mean(mat)
std_dev = np.std(mat)
print("Mean:", mean)
print("Standard Deviation:", std_dev)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
v_stacked = np.vstack((a, b))
h_stacked = np.hstack((a, b))
print("Vertical Stack:\n", v_stacked)
print("Horizontal Stack:\n", h_stacked)

arr = np.random.rand(50)
count = np.sum(arr > 0.5)
print("Count greater than 0.5:", count)
birds = ['spoonbills', 'plovers', 'plovers', 'plovers', 'plovers',
         'Cranes', 'plovers', 'plovers', 'Cranes', 'spoonbills']
age = [5.5, 6.0, 3.5, 1.5, 3.0, 4.0, 3.5, 2.0, 5.5, 6.0]
sorted_birds = [x for _, x in sorted(zip(age, birds))]
print(sorted_birds)

shape = tuple(map(int, input("Enter shape: ").split()))
low, high = map(int, input("Enter low and high: ").split())
arr = np.random.randint(low, high + 1, shape)
print(arr)
