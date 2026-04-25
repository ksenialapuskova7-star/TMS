import random


def random_matrix() -> list:
    M = int(input("Введиите количество строк матрицы: "))
    N = int(input("Введиите количество столбцов матрицы: "))

    matrix = []

    for i in range(M):
        row = []
        for k in range(N):
            row.append(random.randint(1, 20))
        matrix.append(row)
    return matrix


def function_multiplication(matrix: list, k_column: int) -> list:
    count_row = len(matrix)
    count_column = len(matrix[0])

    k_column_elements = []

    for i in matrix:
        k_column_elements.append(i[k_column])

    print("k-столбец:", *k_column_elements, sep=" ")

    i = 0
    while i < count_row:
        for k in range(count_column):
            matrix[i][k] *= k_column_elements[i]
        i += 1
    return matrix


matrix = random_matrix()

print("Исходная матрица:")
for i in matrix:
    for k in i:
        print(f"{k:3d}", end=" ")
    print()

k_column = int(input("Введите номер столбца для перемножения(нумерация с 0): "))

res = function_multiplication(matrix, k_column)

print("Полученная матрица:")
for i in matrix:
    for k in i:
        print(f"{k:3d}", end=" ")
    print()
