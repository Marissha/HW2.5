import random


def get_matrix():
    value = [3, 2, 5, 4, 1, 6]
    n = random.choice(value)
    m = random.choice(value)
    v = random.choice(value)
    return n, m, v
n, m, v = get_matrix()
matrix = []
for i in range(n):
    matrix_1 = []
    for j in range(m):
        matrix_1.append(v)
        matrix.append(matrix_1)
    print(matrix_1)