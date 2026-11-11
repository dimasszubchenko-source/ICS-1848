import os
import tkinter as tk

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'text.txt')


def action1():
    with open(PATH, encoding='utf-8') as f:
        s = f.readline().rstrip('\n')
    result = ''
    for ch in s:
        if not ch.isdigit():
            result += ch
    label_src.config(text='Рядок з файла: ' + s)
    entry.delete(0, tk.END)
    entry.insert(0, result)


win = tk.Tk()
win.title('Видалення цифр з рядка')

frame = tk.Frame(master=win, relief=tk.RAISED, borderwidth=3)
label_src = tk.Label(master=frame, text='Натисніть кнопку, щоб прочитати рядок з файла',
                     wraplength=480)
label = tk.Label(master=frame, text='Рядок без цифр:')
entry = tk.Entry(master=frame, width=70)
button = tk.Button(master=frame, text='ВИДАЛИТИ ЦИФРИ', width=20, command=action1)

frame.pack(padx=10, pady=10)
label_src.pack(pady=5)
label.pack()
entry.pack(padx=10)
button.pack(pady=10)

win.mainloop()
