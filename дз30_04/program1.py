import customtkinter as ctk


class NegativeNumberError(Exception):
    """Исключение, которое возникает при отрицательном числе"""

    pass


def IMT():
    try:
        if not label_height_entry.get() or not label_weight_entry.get():
            label_result.configure(text="Ошибка все поля должны быть заполнены")
            return
        weight = float(label_weight_entry.get())
        height = float(label_height_entry.get())
        if height < 0 or weight < 0:
            raise NegativeNumberError
        IMT = float(round(weight / (height**2), 2))
        if IMT < 16:
            annotation = "выраженный дефицит массы тела"
        elif 16 <= IMT < 18.5:
            annotation = "Недостаточная масса тела"
        elif 18.5 <= IMT < 25:
            annotation = "Нормальная масса тела"
        elif 25 <= IMT < 30:
            annotation = "Избыточная масса тела(предожирение)"
        elif 30 <= IMT < 35:
            annotation = "Ожирение 1-й степени"
        elif 35 <= IMT < 40:
            annotation = "Ожирение 2-й степени"
        elif 40 <= IMT:
            annotation = "Ожирение 3-й степени"
        label_result.configure(text=f"Индекс массы тела = {IMT}\n{annotation}")
    except ZeroDivisionError:
        label_result.configure(text="Ошибка! Деление на ноль")

    except NegativeNumberError:
        label_result.configure(text="Ошибка! Числа должны быть положительными")

    except ValueError:
        label_result.configure(text="Ошибка! Введите числа")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("ИМТ")
window.geometry("300x300")
window.resizable(False, False)

label_height = ctk.CTkLabel(window, text=" Введите рост ")
label_height.pack(pady=10)
label_height_entry = ctk.CTkEntry(
    window,
    placeholder_text="метры",
)
label_height_entry.pack(pady=5)

label_weight = ctk.CTkLabel(window, text=" Введите вес ")
label_weight.pack(pady=5)
label_weight_entry = ctk.CTkEntry(
    window,
    placeholder_text="килограммы",
)
label_weight_entry.pack(pady=5)

bautton_IMT = ctk.CTkButton(window, text="Вычислить ИМТ", command=IMT)
bautton_IMT.pack(pady=10)

label_result = ctk.CTkLabel(
    window,
    fg_color="#031629",
    corner_radius=10,
    text="Результат",
    font=("Arial", 11),
    width=144,
    height=30,
)
label_result.pack(pady=5)


window.mainloop()
