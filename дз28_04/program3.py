n = int(input("Введите количество строк"))
spisok_string = []
for i in range(n):
    s = input(f"Введите строку {i}: ")
    spisok_string.append(s)


def palindrom(x: str) -> str:
    x = x.lower().replace(" ", "")
    res = x[::-1]
    if x == res:
        return "Yes"
    else:
        return "No"


res = list(filter(lambda x: palindrom(x) == "Yes", spisok_string))

print(res)
