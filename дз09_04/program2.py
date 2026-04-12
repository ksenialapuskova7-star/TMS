import tkinter as tk


def calculations():
    i = float(label_i_Entry.get()) / 100
    s = float(label_s_Entry.get())
    n = int(label_n_Entry.get())
    p = round(i / 12, 6)

    m = float(round((s * p * (1 + p) ** n) / ((1 + p) ** n - 1), 4))
    overpayment = round(m * n - s, 2)
    total_fee = round(m * n, 2)

    result_label.configure(
        text=f"\n📊 Сумма ежемесячной выплаты: {m}\n💰 Перепоата: {overpayment}\n💵 Общая выплата: {total_fee}\n"
    )


window = tk.Tk()
window.title("Играл с кредитами = проиграл")
window.geometry("400x500")
window.configure(bg="pink")

frame_i = tk.Frame(window, bg="pink")
frame_i.pack(anchor="w")

label_i = tk.Label(frame_i, text="Введите годовую процентную ставку", bg="pink")
label_i.pack(side="left", pady=10)

label_i_Entry = tk.Entry(frame_i, bg="white", width=20)
label_i_Entry.pack(pady=10)

frame_s = tk.Frame(window, bg="pink")
frame_s.pack(anchor="w", fill="x")

label_s = tk.Label(frame_s, text="Введите сумму займа", bg="pink")
label_s.pack(side="left", pady=10)

label_s_Entry = tk.Entry(frame_s, bg="white")
label_s_Entry.pack(padx=85, pady=10)


frame_n = tk.Frame(window, bg="pink")
frame_n.pack(anchor="w")

label_n = tk.Label(
    frame_n,
    text="Введите количество месяцев",
    bg="pink",
)
label_n.pack(side="left", pady=10)

label_n_Entry = tk.Entry(frame_n, bg="white")
label_n_Entry.pack(padx=45, pady=10)

button_calculate = tk.Button(text="Вычислить", command=calculations)
button_calculate.pack()

result_label = tk.Label(bg="white", relief="ridge", width=34, height=3)
result_label.pack()

window.mainloop()
