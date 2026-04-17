all_sum = int(input("Введите сумму, которую нужно накопить: "))
every_day_sum = int(input("Введите сумму, которую Маша может откладывать: "))

days = 0
sum = 0

while sum < all_sum:
    sum += every_day_sum
    days += 1
    if days % 7 == 0:
        sum -= every_day_sum

print("Количество дней, нужное для накопления = ", days)
