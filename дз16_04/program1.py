from math import factorial, radians

choice = int(input("Что вы хотите вычислить(Введите цифру):\n1. sin(x)\n2. cos(x)\n"))

if choice == 1:
    x = float(input("Введите угол, синус которого нужно вычислить:"))
    n = int(
        input("Введите количество n для точности(чем больше n, тем выше точность): ")
    )

    x = radians(x)
    sin = 0

    for i in range(n):
        sin += (-1) ** i * ((x ** (2 * i + 1)) / (factorial(2 * i + 1)))

    print("Sin = ", round(sin, 3))

if choice == 2:
    x = float(input("Введите угол, косинус которого нужно вычислить:"))
    n = int(
        input("Введите количество n для точности(чем больше n, тем выше точность): ")
    )

    x = radians(x)

    cos = 0

    for i in range(n):
        cos += (-1) ** i * ((x ** (2 * i)) / (factorial(2 * i)))

    print("Cos = ", round(cos, 3))
