s1 = input("Введіть перший рядок слів: ")
s2 = input("Введіть другий рядок слів: ")

words = (s1 + " " + s2).split()

words.sort(key=len, reverse=True)

print("Слова у порядку зменшення довжини:")
for w in words:
    print(w, "-", len(w))
