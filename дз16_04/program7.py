def binary(spisok: list, x: int) -> int:
    n = len(spisok)
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if spisok[mid] > spisok[mid + 1]:
            left = mid + 1
        else:
            right = mid

    mid = left

    if x < spisok[0]:
        left = mid
        right = n - 1
    else:
        left = 0
        right = mid - 1

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
    item = int(input(f"Введите элемент {i} :"))
    spisok.append(item)

print(*spisok, sep=", ")

x = int(input("Введите элемент для поиска: "))

pos = binary(spisok, x)

if pos != -1:
    print(f"Элемент найден на позиции: {pos}")
else:
    print("Элемент не найден")
