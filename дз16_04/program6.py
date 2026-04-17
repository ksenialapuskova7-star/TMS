import random


def binary(spisok: list, x: int) -> int:
    left = 0
    right = len(spisok) - 1
    i = 0
    while left <= right:
        mid = (left + right) // 2
        if x == spisok[mid]:
            return mid
        if x > spisok[mid]:
            left = mid + 1
        if x < spisok[mid]:
            right = mid - 1
    return -1


spisok = []
n = int(input("Введите количество элементов списка: "))

for i in range(n):
    spisok.append(random.randint(1, 15))

spisok.sort()

print(*spisok, sep=", ")

x = int(input("Введите элемент для поиска: "))

pos = binary(spisok, x)

if pos != -1:
    print(f"Элемент найден на позиции: {pos}")
else:
    print("Элемент не найден")
