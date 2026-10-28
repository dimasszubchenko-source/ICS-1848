import string

f = open("fragment.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

# видаляємо зайві пробіли і порожні рядки
clean = []
for line in lines:
    line = " ".join(line.split())
    if line != "":
        clean.append(line)

# записуємо результат у новий файл
f = open("fragment_clean.txt", "w", encoding="utf-8")
for line in clean:
    f.write(line + "\n")
f.close()

# рахуємо оригінальні слова
words = set()
for line in clean:
    for w in line.split():
        w = w.strip(string.punctuation).lower()
        if w != "":
            words.add(w)

print("Текст після видалення зайвих пробілів:")
for line in clean:
    print(line)
print("Кількість оригінальних слів:", len(words))
print("Кількість рядків тексту:", len(clean))
