def prime_number(number: int) -> str:
    if number < 0:
        return f"Простота определяется только для положительных целых чисел, а {number} является отрицательным"
    if number == 1 or number == 0:
        return f"{number} не является ни простым ни составным"
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        return f"Число {number} является простым"
    else:
        return f"Число {number} не является простым(составное)"


number = int(input("Введите целое число для проверки на простоту"))

res = prime_number(number)

print(res)
