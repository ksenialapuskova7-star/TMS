import random


def random_matrix() -> list:
    M = int(input("Введите количество строк матрицы: "))
    N = int(input("Введите количество столбцов матрицы: "))

    matrix = []

    for i in range(M):
        row = []
        for k in range(N):
            row.append(random.randint(0, 1))
        matrix.append(row)

    return matrix


def add_parity_column(matrix: list) -> list:
    count_row = len(matrix)
    count_column = len(matrix[0])

    for i in range(count_row):
        count = 0
        for k in range(count_column):
            if matrix[i][k] == 1:
                count += 1
        if count % 2 == 1:
            matrix[i].append(1)
        else:
            matrix[i].append(0)

    return matrix


matrix = random_matrix()

print("Исходная матрица:")
for i in matrix:
    for k in i:
        print(f"{k:3d}", end=" ")
    print()

res = add_parity_column(matrix)

print("Полученная матрица:")
for i in res:
    for k in i:
        print(f"{k:3d}", end=" ")
    print()
