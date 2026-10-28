import os

names = ["report_1.docx", "report_2.docx", "notes.txt", "todo.txt",
         "photo1.jpg", "photo2.jpg", "photo3.png", "song.mp3",
         "lecture.pdf", "task.pdf", "lab9.py", "lab10.py",
         "table.xlsx", "presentation.pptx", "data.csv"]

if not os.path.exists("MY_FILES"):
    os.mkdir("MY_FILES")
for name in names:
    f = open(os.path.join("MY_FILES", name), "w", encoding="utf-8")
    f.write("Тестовий файл " + name)
    f.close()
print("Створено файлів:", len(names))
