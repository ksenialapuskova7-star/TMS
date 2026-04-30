import random

n = int(input("Введите количество чисел: "))

spisok = [random.randint(-20, 20) for i in range(n)]
print(list(map(lambda x: str(x), spisok)))
