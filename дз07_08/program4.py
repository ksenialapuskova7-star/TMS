stroka = input("Введите строку: ")

stroka = list(stroka.upper())

for i in range(0, len(stroka), 1):
    if stroka[i] == "H":
        stroka[i] = "h"
        break
for i in range(len(stroka) - 1, -1, -1):
    if stroka[i] == "H":
        stroka[i] = "h"
        break

stroka = "".join(stroka)

print(stroka)
