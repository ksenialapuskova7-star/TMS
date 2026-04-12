import tkinter as tk
from PIL import Image, ImageTk
from math import cos, sin, sqrt


def show_main_menu():
    for widget in window.winfo_children():
        widget.destroy()

    label_choice = tk.Label(
        window, text="Выберите вариант(Кликните на картинку)", bg="pink"
    )
    label_choice.pack(pady=30)

    button_a = tk.Button(window, anchor="w", image=photo_a, command=choice_button_a)
    button_a.pack(pady=10)

    button_b = tk.Button(window, anchor="w", image=photo_b, command=choice_button_b)
    button_b.pack(pady=10)

    button_c = tk.Button(window, anchor="w", image=photo_c, command=choice_button_c)
    button_c.pack(pady=10)

    button_d = tk.Button(window, anchor="w", image=photo_d, command=choice_button_d)
    button_d.pack(pady=10)


def choice_button_a():
    def but_calcul():

        a = int(a_entry.get())

        b = int(b_entry.get())

        res = (
            (a**2) / 3 + (a**2 + 4) / b + (a**2 + 4) ** 0.5 / 4 + (a**2 + 4) ** 1.5 / 4
        )
        res = round(res, 2)

        result_label.config(text=f"{res}")

    for widget in window.winfo_children():
        widget.destroy()

    label_photo_a = tk.Label(window, image=photo_a, bg="pink")
    label_photo_a.pack(side="top", pady=10)

    label_input_a = tk.Label(window, text="Введите а", bg="pink", font=("Arial", 14))
    label_input_a.pack()
    a_entry = tk.Entry(window, relief="ridge")
    a_entry.pack()

    label_input_b = tk.Label(window, text="Введите b", bg="pink", font=("Arial", 14))
    label_input_b.pack()
    b_entry = tk.Entry(window, relief="ridge")
    b_entry.pack()

    button_calculations = tk.Button(
        window, pady=10, text="Вычислить", bg="lightgray", command=but_calcul
    )
    button_calculations.pack(pady=20)
    result_label = tk.Label(
        window,
        bg="white",
        height=1,
        width=15,
        relief="ridge",
        font=("Arial", 10),
    )
    result_label.pack()

    back_button = tk.Button(
        window,
        text="← Назад",
        command=show_main_menu,
        bg="lightgray",
        font=("Arial", 10),
    )
    back_button.pack(pady=10)


def choice_button_b():
    def but_calcul():

        x = int(x_entry.get())

        res = cos(x) + sin(x)

        res = round(res, 2)

        result_label.config(text=f"{res}", relief="groove", bd="3")

    for widget in window.winfo_children():
        widget.destroy()

    label_photo_b = tk.Label(window, image=photo_b, bg="pink")
    label_photo_b.pack(side="top", pady=10)

    label_input_x = tk.Label(window, text="Введите х", bg="pink", font=("Arial", 14))
    label_input_x.pack()
    x_entry = tk.Entry(window)
    x_entry.pack()

    button_calculations = tk.Button(
        window, pady=10, text="Вычислить", bg="lightgray", command=but_calcul
    )
    button_calculations.pack(pady=20)

    result_label = tk.Label(
        window,
        bg="white",
        height=1,
        width=15,
        relief="ridge",
        font=("Arial", 10),
    )
    result_label.pack()
    back_button = tk.Button(
        window,
        text="← Назад",
        command=show_main_menu,
        bg="lightgray",
        font=("Arial", 10),
    )
    back_button.pack(pady=10)


def choice_button_c():
    def but_calcul():

        x = float(x_entry.get())

        res = (cos(x**2) ** 2 + sin(2 * x - 1) ** 2) ** (1 / 3)

        res = round(res, 2)

        result_label.config(text=f"Результат: {res}", relief="groove", bd="3")

    for widget in window.winfo_children():
        widget.destroy()

    label_photo_c = tk.Label(window, image=photo_c, bg="pink")
    label_photo_c.pack(side="top", pady=10)

    label_input_x = tk.Label(window, text="Введите х", bg="pink", font=("Arial", 14))
    label_input_x.pack()
    x_entry = tk.Entry(window)
    x_entry.pack()

    button_calculations = tk.Button(
        window,
        anchor="w",
        pady=10,
        text="Вычислить",
        bg="lightgray",
        command=but_calcul,
    )
    button_calculations.pack(pady=20)

    result_label = tk.Label(
        window,
        bg="white",
        height=1,
        width=15,
        relief="ridge",
        font=("Arial", 10),
    )
    result_label.pack()
    back_button = tk.Button(
        window,
        text="← Назад",
        command=show_main_menu,
        bg="lightgray",
        font=("Arial", 10),
    )
    back_button.pack(pady=10)


def choice_button_d():
    def but_calcul():

        x = float(x_entry.get())

        res = 5 * x + 3 * x * x * sqrt(1 + sin(x) ** 2)

        res = round(res, 2)

        result_label.config(text=f"Результат: {res}", relief="groove", bd="3")

    for widget in window.winfo_children():
        widget.destroy()

    label_photo_d = tk.Label(window, image=photo_d, bg="pink")
    label_photo_d.pack(side="top", pady=10)

    label_input_x = tk.Label(window, text="Введите х", bg="pink", font=("Arial", 14))
    label_input_x.pack()
    x_entry = tk.Entry(window)
    x_entry.pack()

    button_calculations = tk.Button(
        window, pady=10, text="Вычислить", bg="lightgray", command=but_calcul
    )
    button_calculations.pack(pady=20)

    result_label = tk.Label(
        window,
        bg="white",
        height=1,
        width=15,
        relief="ridge",
        font=("Arial", 10),
    )
    result_label.pack()
    back_button = tk.Button(
        window,
        text="← Назад",
        command=show_main_menu,
        bg="lightgray",
        font=("Arial", 10),
    )
    back_button.pack(pady=10)


window = tk.Tk()
window.title("Вычисление математических выражений")
window.geometry("400x500")
window.configure(bg="pink")

label_choice = tk.Label(
    window,
    text="Выберите вариант(Кликните на картинку)",
    bg="pink",
    font="Helvetica",
)
label_choice.pack(pady=30)
image_a = Image.open("pictures/Picture_a.png")
small_image_a = image_a.resize((300, 60))
photo_a = ImageTk.PhotoImage(small_image_a)
button_a = tk.Button(window, anchor="w", image=photo_a, command=choice_button_a)
button_a.pack(pady=10)

image_b = Image.open("pictures/Picture_b.png")
small_image_b = image_b.resize((300, 60))
photo_b = ImageTk.PhotoImage(small_image_b)
button_b = tk.Button(window, anchor="w", image=photo_b, command=choice_button_b)
button_b.pack(pady=10)

image_c = Image.open("pictures/Picture_c.png")
small_image_c = image_c.resize((300, 60))
photo_c = ImageTk.PhotoImage(small_image_c)
button_c = tk.Button(window, anchor="w", image=photo_c, command=choice_button_c)
button_c.pack(pady=10)

image_d = Image.open("pictures/Picture_d.png")
small_image_d = image_d.resize((300, 60))
photo_d = ImageTk.PhotoImage(small_image_d)
button_d = tk.Button(window, anchor="w", image=photo_d, command=choice_button_d)
button_d.pack(pady=10)

window.mainloop()
