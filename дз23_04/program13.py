import random


def random_matrix() -> list:
    N = int(input("Введите количество строк = количеству столбцов матрицы: "))

    matrix = []

    for i in range(N):
        row = []
        for k in range(N):
            row.append(random.randint(1, 15))
        matrix.append(row)

    return matrix


def side_diagonal_sum(matrix: list) -> int:
    count_row_column = len(matrix)
    all_sum = sum(matrix[count_row_column - i - 1][i] for i in range(count_row_column))
    return all_sum


def main_diagonal_sum(matrix: list) -> int:
    count_row_column = len(matrix)
    all_sum = sum(matrix[i][i] for i in range(count_row_column))
    return all_sum


matrix = random_matrix()

print("Исходная матрица:")
for i in matrix:
    for k in i:
        print(f"{k:3d}", end=" ")
    print()

print(
    f"Сумма элементов главной диагонали = {main_diagonal_sum(matrix)}\nСумма элементов побочной диагонали = {side_diagonal_sum(matrix)}"
)
