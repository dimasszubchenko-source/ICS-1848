import csv

f = open("text.txt", "r", encoding="utf-8")
text = f.read().lower()
f.close()

# рахуємо всі літери в тексті
total = 0
for ch in text:
    if ch.isalpha():
        total += 1

# рахуємо кожну голосну літеру
vowels = "aeiou"
rows = []
for v in vowels:
    count = text.count(v)
    percent = round(count / total * 100, 2)
    rows.append([v, count, percent])

# записуємо дані у файл CSV
f = open("vowels.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(f)
writer.writerow(["letter", "count", "frequency_%"])
writer.writerows(rows)
f.close()

# зчитуємо файл і виводимо на екран
print("Усього літер у тексті:", total)
print("Вміст файлу vowels.csv:")
f = open("vowels.csv", "r", newline="", encoding="utf-8")
reader = csv.reader(f)
for row in reader:
    print(row)
f.close()
