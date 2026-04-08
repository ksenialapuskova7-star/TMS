a = int(input("Введите число a = "))
b = int(input("Введите число b = "))
c = int(input("Введите число c = "))

print("\nРезультаты вычислений:")
print(
    "a + b + c = ",
    a + b + c,
    "\na - b - c = ",
    a - b - c,
    "\na * b * c = ",
    a * b * c,
    "\na - b + c = ",
    a - b + c,
    "\na * b / c = ",
    round(a * b / c, 2),
    "\n(a + b) % c = ",
    (a + b) % c,
)
