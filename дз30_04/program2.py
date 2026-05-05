import customtkinter as ctk


def operation_plus():
    try:
        x = float(label_x_entry.get())
        y = float(label_y_entry.get())
        result = x + y
        if result == int(result):
            result = int(result)
        label_result.configure(text=f"{x} + {y} = {result}")
    except ValueError:
        label_result.configure(text="Ошибка! Введите числа")
    except:
        label_result.configure(text="Ошибка! Заполните поля")


def operation_minus():
    try:
        x = float(label_x_entry.get())
        y = float(label_y_entry.get())
        result = x - y
        if result == int(result):
            result = int(result)
        label_result.configure(text=f"{x} - {y} = {result}")
    except ValueError:
        label_result.configure(text="Ошибка! Введите числа")
    except:
        label_result.configure(text="Ошибка! Заполните поля")


def operation_multiplication():
    try:
        x = float(label_x_entry.get())
        y = float(label_y_entry.get())
        result = x * y
        if result == int(result):
            result = int(result)
        label_result.configure(text=f"{x} × {y} = {result}")
    except ValueError:
        label_result.configure(text="Ошибка! Введите числа")
    except:
        label_result.configure(text="Ошибка! Заполните поля")


def operation_division():
    try:
        x = float(label_x_entry.get())
        y = float(label_y_entry.get())
        if y == 0:
            label_result.configure(text="Ошибка! Деление на ноль")
            return
        result = x / y
        if result == int(result):
            result = int(result)
            label_result.configure(text=f"{x} ÷ {y} = {result}")
        else:
            label_result.configure(text=f"{x} ÷ {y} = {result:.4f}")
    except ValueError:
        label_result.configure(text="Ошибка! Введите числа")
    except:
        label_result.configure(text="Ошибка! Заполните поля")


def operation_exponentiation():
    try:
        x = float(label_x_entry.get())
        y = float(label_y_entry.get())
        result = x**y
        if result > 1e10:
            label_result.configure(text=f"{x} ^ {y} = {result:.2e}")
        elif result == int(result):
            label_result.configure(text=f"{x} ^ {y} = {int(result)}")
        else:
            label_result.configure(text=f"{x} ^ {y} = {result}")
    except ValueError:
        label_result.configure(text="Ошибка! Введите числа")
    except OverflowError:
        label_result.configure(text="Ошибка! Слишком большой результат")
    except:
        label_result.configure(text="Ошибка! Заполните поля")


def operation_remainder_from_division():
    try:
        x = float(label_x_entry.get())
        y = float(label_y_entry.get())
        if y == 0:
            label_result.configure(text="Ошибка! Деление на ноль")
            return
        result = x % y
        if result == int(result):
            result = int(result)
        label_result.configure(text=f"{x} % {y} = {result}")
    except ValueError:
        label_result.configure(text="Ошибка! Введите числа")
    except:
        label_result.configure(text="Ошибка! Заполните поля")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("Калькулятор")
window.geometry("400x400")
window.resizable(False, False)

top_frame = ctk.CTkFrame(window)
top_frame.pack(pady=(30, 10))

frame_x = ctk.CTkFrame(top_frame, width=205)
frame_x.pack(side="left", padx=20, pady=20)
label_x = ctk.CTkLabel(frame_x, text=" Введите x ")
label_x.pack(anchor="w")
label_x_entry = ctk.CTkEntry(frame_x, placeholder_text="Введите число")
label_x_entry.pack()

frame_y = ctk.CTkFrame(top_frame, width=205)
frame_y.pack(side="right", padx=20, pady=20)
label_y = ctk.CTkLabel(frame_y, text=" Введите y ")
label_y.pack(anchor="w")
label_y_entry = ctk.CTkEntry(frame_y, placeholder_text="Введите число")
label_y_entry.pack()
label_operation = ctk.CTkLabel(window, text="Выберите операцию")
label_operation.pack()

frame_calculations = ctk.CTkFrame(window, width=400)
frame_calculations.pack(pady=20)

frame_left = ctk.CTkFrame(
    frame_calculations,
    width=100,
    height=50,
)
frame_left.pack(side="left", padx=5)

frame_right = ctk.CTkFrame(frame_calculations, width=300, height=50)
frame_right.pack(side="left", padx=5)
bautton_plus = ctk.CTkButton(frame_left, text="+", command=operation_plus)
bautton_plus.pack(pady=5)
bautton_minus = ctk.CTkButton(frame_left, text="-", command=operation_minus)
bautton_minus.pack(pady=5)
bautton_multiplication = ctk.CTkButton(
    frame_left, text="*", command=operation_multiplication
)
bautton_multiplication.pack(pady=5)
bautton_division = ctk.CTkButton(frame_right, text="/", command=operation_division)
bautton_division.pack(pady=5)
bautton_exponentiation = ctk.CTkButton(
    frame_right, text="^", command=operation_exponentiation
)
bautton_exponentiation.pack(pady=5)
bautton_remainder_from_division = ctk.CTkButton(
    frame_right, text="%", command=operation_remainder_from_division
)
bautton_remainder_from_division.pack(pady=5)

label_result = ctk.CTkLabel(
    window,
    fg_color="#031629",
    corner_radius=10,
    text="Результат",
    font=("Arial", 14, "bold"),
    width=350,
    height=50,
)
label_result.pack(pady=5)


window.mainloop()
