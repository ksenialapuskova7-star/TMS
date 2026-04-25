def binary(spisok: list, element: int, left: int = 0, right: int = None) -> int:
    if right == None:
        right = len(spisok) - 1
    if left > right:
        return -1
    m = (left + right) // 2
    if spisok[m] == element:
        return m
    if element > spisok[m]:
        return binary(spisok, element, m + 1, right)
    if element < spisok[m]:
        return binary(spisok, element, left, m - 1)


spisok = []
n = int(input("Введите количество элементов списка:"))

for i in range(n):
    x = int(input(f"Введите {i}элемент списка:"))
    spisok.append(x)

spisok.sort()

find_number = int(input("Введите элемент из списка для поиска "))

position = binary(spisok, find_number)

if position == -1:
    print("Элемент не найден")
else:
    print(f"Элемент {find_number} найден на позиции {position}")
