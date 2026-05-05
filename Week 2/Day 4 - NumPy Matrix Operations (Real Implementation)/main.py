import numpy as np

W1 = np.array([
    [1, 2],
    [3, 4]
])

W2 = np.array([
    [2, 0],
    [1, 2]
])

x = np.array([5, 6])
x1 = np.array([5, 6, 7])

print(W1.shape)
print(W2.shape)
print(x.shape)
print(x1.shape)
h = np.dot(W1, x)

y = np.dot(W2, h)

print("Output:", y)

np.dot(W1, x1)  # This will raise an error due to shape mismatch