import numpy as np

# Температура
np_arr = np.array([4, 1, 0, -2, 5, 7, -3, 0, 0, 5, 0, -1])
print(np_arr)
print(sum(np_arr < 0))
print(np_arr.argmax())
print(np_arr.any() > 10)
print(np_arr.all() < 10)

print(np.where(np_arr < 0))
np_arr.sort()
print(np_arr)

print("-" * 20)

# Дії з матрицями
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print()
print(a[0, :])
print(a[:, 1])

print()
matrixA = np.array([[1, 2], [3, 4]])
matrixB = np.array([[5, 6], [7, 8]])
print(matrixA.dot(matrixB))

print()
vector = np.array([3, 0])
print(matrixA.dot(vector))
print()

np_matrix = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np_matrix)

print()

A = np.matrix([[4, 5], [8, 0]])
B = np.matrix([[2, 7], [0, 2]])
print(A + B)
print(A.dot(B))

print()
A_t = A.transpose()
print(A)
print(A_t)

A_t2 = A_t.transpose()
print(A_t2 == A)

print(np.linalg.det(A))
print(np.linalg.inv(A))
print(np.linalg.matrix_rank(A))

a = np.array([[3, 7], [1, 5]])
b = np.array([22, 9])
x = np.linalg.solve(a, b)
print(x)

print("-" * 20)

# Дії з векторами
vecA = np.array([1, 0])
vecB = np.array([2, 2])
print(vecA + vecB)
print(vecB - vecA)
print(vecA * 2)
print(vecA.dot(vecB))
print(np.linalg.norm(vecA))
print(np.linalg.norm(vecB - vecA))
print(np.dot(vecA, vecB) / (np.linalg.norm(vecA) * (np.linalg.norm(vecB))))
print(np.shape(vecA))
