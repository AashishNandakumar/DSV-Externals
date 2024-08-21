# describe different numpy operations
import numpy as np

# array creation
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.ones((2, 2))
d = np.zeros((3, 3))
e = np.arange(0, 10, 2)
# print(e)
# print(b)
# print(c)

# array opertions (vector operations - applies to each element)
# print(a + 1)
# print(a * 2)
# print(a**3)
# print(np.sqrt(a))

# array indexing and slicing
# print(a[0])
# print(b[0, 1])  # 1st row and 2nd column(0 indexing)
# print(b[:, 1])  # every rows and 2nd column
# print(a[:])

# array shape manipulation
# print(a.reshape(3, 1))  # convert it into 3*1 matrix
# print(b.flatten())  # convert 2d array to 1d array

# statistical operations
# print(np.sum(a))
# print(np.mean(a))
# print(np.max(a))
# print(np.min(a))
# print(np.median(a))

# linear algebra
# print(np.dot(a, a))  # dot product
# print(np.linalg.inv(b))  # inverse of a matrix
# print(np.linalg.eig(b))  # eigen value and eigen vectors of a matrix

# random number generation
print(np.random.rand(3, 3))  # produce a 3*3 matrix of random values bw 0 and 1
print(
    np.random.randn(3, 3)
)  # produce a 3*3 matrix of random numbers from standard normal distribution
