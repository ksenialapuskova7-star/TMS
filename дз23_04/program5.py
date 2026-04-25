def encryption_decryption(choice: str, s: str, language: str, shift: int) -> str:
    n_s = len(s)
    alphabet = []
    if language == "R":
        alphabet = list(
            "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
        )
    if language == "E":
        alphabet = list("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
    n_alphabet = len(alphabet)
    s2 = []
    for i in range(n_s):
        found = False
        for k in range(n_alphabet):
            if s[i] == alphabet[k]:
                found = True
                if choice == "Enc":
                    x = (k + shift * 2) % n_alphabet
                else:
                    x = (k - shift * 2) % n_alphabet
                s2.append(alphabet[x])
                break
        if not found:
            s2.append(s[i])
    return "".join(s2)


choice = input("Выберите действие со строкой: Enc(шифровка) или Dec(расшифровка)")

s = input("Введите строку: ")
language = input("Введите язык: R(русский) или E(английский): ")
shift = int(input("Введите сдвиг: "))

res = encryption_decryption(choice, s, language, shift)

print(res)
