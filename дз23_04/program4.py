def Greatest_Common_Divisor(number_1: int, number_2: int) -> str:
    list_number_1 = []
    list_number_2 = []
    list_find_max_divisor = []
    for i in range(1, number_1 + 1):
        if number_1 % i == 0:
            list_number_1.append(i)
    for i in range(1, number_2 + 1):
        if number_2 % i == 0:
            list_number_2.append(i)
    n_len_1 = len(list_number_1)
    n_len_2 = len(list_number_2)
    for i in range(n_len_1):
        for k in range(n_len_2):
            if list_number_1[i] == list_number_2[k]:
                x = list_number_1[i]
                list_find_max_divisor.append(x)
    if list_find_max_divisor:
        maximum = max(list_find_max_divisor)
        return f"Наибольший общий делитель чисел {number_1} и {number_2} = {maximum}"
    else:
        return f"Числа {number_1} и {number_2} не имеют общих делителей"


number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))

res = Greatest_Common_Divisor(number_1, number_2)

print(res)
