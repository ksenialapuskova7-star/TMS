import random


def random_matrix() -> list:
    M = int(input("Введите количество строк матрицы: "))
    N = int(input("Введите количество столбцов матрицы: "))

    matrix = []

    for i in range(M):
        row = []
        for k in range(N):
            row.append(random.randint(1, 15))
        matrix.append(row)

    return matrix


def column_with_h(matrix: list, h: int) -> list:

    count_row = len(matrix)
    count_column = len(matrix[0])

    column = []

    k = 0
    while k < count_column:
        for i in range(count_row):
            if matrix[i][k] == h:
                column.append(k)
                break
        k += 1

    return column


matrix = random_matrix()

print("Исходная матрица:")

for i in matrix:
    for k in i:
        print(f"{k:3d}", end=" ")
    print()

h = int(input("Введите число для поиска в столбцах: "))

res = column_with_h(matrix, h)
if res:
    print(f"Элемент {h} находится в столбцах:", end=" ")
    print(*res, sep=", ")
else:
    print(f"Числа {h} нет ни в одном из столбцов")
