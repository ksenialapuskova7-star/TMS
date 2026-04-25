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


def sum_all_matrix(matrix: list) -> int:
    sum_all = sum(sum(i) for i in matrix)
    return sum_all


matrix = random_matrix()

print("Матрица:")
for i in matrix:
    for element in i:
        print(f"{element:3d}", end=" ")
    print()

sum_all = sum_all_matrix(matrix)
print(f"Сумма всех элементов матрицы: {sum_all}")


N = len(matrix[0])

sum_column_matrix = []
for i in range(N):
    sum_column_matrix.append(0)

for rows in matrix:
    for k in range(N):
        sum_column_matrix[k] += rows[k]


for k in range(len(sum_column_matrix)):
    print(
        f"Сумма {k} столбца = {sum_column_matrix[k]} - это {round(sum_column_matrix[k]*100/sum_all, 2)}% от общей суммы"
    )
