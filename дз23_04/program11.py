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


def function_sum(matrix: list, l_row: int) -> list:
    count_column = len(matrix[0])

    elements_l_row = matrix[l_row]

    for i in matrix:
        for k in range(count_column):
            i[k] += elements_l_row[k]

    return matrix


matrix = random_matrix()

print("Исходная матрица:")
for i in matrix:
    for k in i:
        print(f"{k:3d}", end=" ")
    print()

l_row = int(input("Введите номер строки для суммирования(нумерация с 0): "))

res = function_sum(matrix, l_row)

print("Полученная матрица:")
for i in matrix:
    for k in i:
        print(f"{k:3d}", end=" ")
    print()
