import os
import shutil

folder = "MY_FILES"

# перебираємо всі файли в каталозі
for name in sorted(os.listdir(folder)):
    path = os.path.join(folder, name)
    if os.path.isfile(path):
        # розширення файла без крапки
        ext = os.path.splitext(name)[1][1:].lower()
        new_dir = os.path.join(folder, ext)
        # якщо папки ще немає, створюємо її
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        shutil.move(path, os.path.join(new_dir, name))
        print("Файл", name, "переміщено в папку", ext)

print("Вміст каталогу після виконання:")
for d in sorted(os.listdir(folder)):
    print(d + ":", sorted(os.listdir(os.path.join(folder, d))))
