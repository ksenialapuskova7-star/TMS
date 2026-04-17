import random

listik = []

n = int(input("Введите количество элементов списка: "))

summa = 0

for i in range(n):
    listik.append(random.randint(1, 15))

print("Список:\n", *listik)
minimum = listik[0]
maximum = listik[0]

for i in range(n):
    summa += listik[i]
    if listik[i] < minimum:
        minimum = listik[i]
    if listik[i] > maximum:
        maximum = listik[i]

print(
    "Сумма элементов списка = ",
    summa,
    "\nНаибольший элемент списка = ",
    maximum,
    "\nНаименьший элемент списка: ",
    minimum,
)
