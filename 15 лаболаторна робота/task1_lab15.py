import json
import os
import tkinter as tk

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'start.json')
with open(PATH, encoding='utf-8') as f:
    workers = json.load(f)


def show_all():
    text_box.delete('1.0', tk.END)
    for w in workers:
        text_box.insert(tk.END, w['surname'] + ' - ' + str(w['salary']) + ' грн\n')


def show_salary():
    surname = entry.get().strip().lower()
    for w in workers:
        if w['surname'].lower() == surname:
            result.config(text='Заробітна плата: ' + str(w['salary']) + ' грн')
            return
    result.config(text='Робітника не знайдено')


win = tk.Tk()
win.title('Довідник робітників')
win.geometry('400x350')
win.configure(background='green')

label = tk.Label(text='Введіть прізвище робітника:', background='green', foreground='white')
entry = tk.Entry(width=30)
button1 = tk.Button(text='Показати зарплату', width=25, command=show_salary)
result = tk.Label(text='', background='green', foreground='white')
button2 = tk.Button(text='Показати всіх робітників', width=25, command=show_all)
text_box = tk.Text(width=45, height=12, font=('Consolas', 9))

label.pack()
entry.pack()
button1.pack()
result.pack()
button2.pack()
text_box.pack()

win.mainloop()
