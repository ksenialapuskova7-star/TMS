import random

n = int(input("Введите количество элементов списка: "))

spisok = []

for i in range(n):
    spisok.append(random.randint(1, 15))

print(*spisok, sep=", ")

temporary = set()
k = 0

while k < n:
    count = 0
    item = spisok[k]

    if item not in temporary:
        for i in range(n):
            if spisok[k] == spisok[i]:
                count += 1

    if count > 1:
        temporary.add(item)
        print(f"Элемент списка {item} встречается {count} ")

    k += 1
