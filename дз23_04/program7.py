import random


def random_matrix():
    M = int(input("Введиите количество строк матрицы: "))
    N = int(input("Введиите количество столбцов матрицы: "))

    matrix = []

    for i in range(M):
        row = []
        for k in range(N):
            row.append(random.randint(1, 100))
        matrix.append(row)
    return matrix


res = random_matrix()

for i in res:
    print(*i)
