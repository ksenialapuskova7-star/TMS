import random

n = int(input("Введите количество чисел: "))

spisok = [random.randint(-20, 20) for i in range(n)]
print(*spisok)
res = list(filter(lambda x: x > 0, spisok))
print(*res)
