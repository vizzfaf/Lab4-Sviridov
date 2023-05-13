import numpy as np
import time


class MultidimensionalArray:
    def __init__(self, shape):
        self.array = np.zeros(shape)
        self.rows, self.cols = shape

    def direct_access(self, i, j):
        return self.array[i][j]

    def vector_access(self, i, j):
        if i >= self.rows or j >= self.cols:
            return None
        index = i * self.cols + j
        return self.array.flatten()[index]

    def determinant_vectors(self):
        row_vectors = [self.array[i] for i in range(self.rows)]
        col_vectors = [self.array[:, j] for j in range(self.cols)]
        return row_vectors, col_vectors



B = MultidimensionalArray((100, 200))


start = time.time()
for i in range(100):
    for j in range(200):
        B.direct_access(i, j)
end = time.time()
print("Direct access time:", end - start, "seconds")

start = time.time()
for i in range(100):
    for j in range(200):
        B.vector_access(i, j)
end = time.time()
print("Vector access time:", end - start, "seconds")


import sys
direct_access_mem = sys.getsizeof(B.array)
determinant_vectors_mem = sys.getsizeof(B.determinant_vectors())
print("Memory usage of direct access:", direct_access_mem, "bytes")
print("Memory usage of determinant vectors:", determinant_vectors_mem, "bytes")
