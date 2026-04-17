n = int(input("Введите количество членов последовательности: "))

fibbohachi = []

for i in range(0, n):
    if i == 0 or i == 1:
        fibbohachi.append(1)
    else:
        fibbohachi.append(fibbohachi[i - 1] + fibbohachi[i - 2])

print(*fibbohachi, sep=", ")
