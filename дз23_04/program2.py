def conversion(number: int, binary: str = "") -> str:
    if number <= 1:
        return binary + str(number)
    remainder = number % 2
    integer = number // 2
    binary += str(remainder)
    return conversion(integer, binary)


number = int(
    input("введите число в 10-тичной системе исчисления для перевода в 2-ичную: ")
)
res = conversion(number)
res = res[::-1]
print(f"Число {number} в двоичной системе исчисления = {res}")
