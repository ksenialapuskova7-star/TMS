def encryption_decryption(choice: str, s: str, language: str, key: str) -> str:
    s = s.lower()
    key = key.lower()
    n_s = len(s)
    n_key = len(key)
    alphabet = []
    if language == "R":
        alphabet = list("абвгдежзийклмнопрстуфхцчшщъыьэюя")
    if language == "E":
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
    n_alphabet = len(alphabet)
    s2 = []
    for i in range(n_s):
        key_now = key[i % n_key]
        shift = 0
        found = False
        for j in range(n_alphabet):
            if key_now == alphabet[j]:
                shift = j
        for k in range(n_alphabet):
            if s[i] == alphabet[k]:
                found = True
                if choice == "Enc":
                    x = (k + shift) % n_alphabet
                else:
                    x = (k - shift) % n_alphabet
                s2.append(alphabet[x])
                break
        if not found:
            s2.append(s[i])
    return "".join(s2)


choice = input("Выберите действие со строкой: Enc(шифровка) или Dec(расшифровка)")

s = input("Введите строку: ")
language = input("Введите язык: R(русский) или E(английский): ")
key = input("Введите строку-ключ: ")

res = encryption_decryption(choice, s, language, key)

print(res)
