import tkinter as tk
from math import pi


def calculations():
    try:
        if (
            not R1_Entry.get()
            or not R2_Entry.get()
            or not V1_Entry.get()
            or not V2_Entry.get()
        ):
            result_label.configure(text="Ошибка! Заполните все поля")
            return

        r1 = float(R1_Entry.get())
        r2 = float(R2_Entry.get())
        v1 = float(V1_Entry.get())
        v2 = float(V2_Entry.get())

        l1 = round((2 * r1 * pi) / v1, 2)
        l2 = round((2 * r2 * pi) / v2, 2)

        if (l1 - l2) > 0:
            difference = "Длина светового года планеты 1 больше,\nчем на Планете 2"
        else:
            difference = "Длина светового года на планете 1 меньше,\nчем на планете 2"

        result_label.configure(
            text=f"Длина года на планете 1: {l1}\nДлина года на планете 2: {l2}\n{difference}"
        )

    except ValueError:
        result_label.configure(text="Ошибка! Введите числа")
    except ZeroDivisionError:
        result_label.configure(text="Ошибка! Деление на ноль")


window = tk.Tk()
window.title("Интерстеллар")
window.geometry("330x500")
window.configure(bg="pink")

label_Planet_1 = tk.Label(window, text="Планета 1", bg="lightblue", relief="ridge")
label_Planet_1.pack(pady=10)

frame_R1 = tk.Frame(window, bg="pink")
frame_R1.pack(pady=5)

label_R1 = tk.Label(
    frame_R1,
    text="Радиус планеты 1                             ",
    bg="silver",
    relief="groove",
)
label_R1.pack(side="left", pady=5)

R1_Entry = tk.Entry(frame_R1, bg="white")
R1_Entry.pack(side="left")

frame_V1 = tk.Frame(window, bg="pink")
frame_V1.pack(pady=5)

label_V1 = tk.Label(
    frame_V1, text="Орбитальная скорость планеты 1", bg="silver", relief="groove"
)
label_V1.pack(side="left", pady=10)

V1_Entry = tk.Entry(frame_V1, bg="white")
V1_Entry.pack(pady=10)


label_Planet_2 = tk.Label(window, text="Планета 2", bg="lightblue", relief="ridge")
label_Planet_2.pack(pady=10)

frame_R2 = tk.Frame(window, bg="pink")
frame_R2.pack(pady=5)

label_R2 = tk.Label(
    frame_R2,
    text="Радиус планеты 2                             ",
    bg="silver",
    relief="groove",
)
label_R2.pack(side="left", pady=5)

R2_Entry = tk.Entry(frame_R2, bg="white")
R2_Entry.pack(side="left")

frame_V2 = tk.Frame(window, bg="pink")
frame_V2.pack(pady=5)

label_V2 = tk.Label(
    frame_V2, text="Орбитальная скорость планеты 2", bg="silver", relief="groove"
)
label_V2.pack(side="left", pady=5)

V2_Entry = tk.Entry(frame_V2, bg="white")
V2_Entry.pack(pady=5)


button_calculate = tk.Button(text="Вычислить", command=calculations)
button_calculate.pack(pady=0)

result_label = tk.Label(
    anchor="w", justify="left", bg="white", relief="ridge", width=35, height=4
)
result_label.pack(pady=10)

window.mainloop()
