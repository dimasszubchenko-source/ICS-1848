# функція, яка читає словник з файла і повертає його
def read_dict(filename):
    d = {}
    f = open(filename, "r", encoding="utf-8")
    for line in f:
        line = line.strip()
        if line != "":
            key, value = line.split(":")
            d[key] = value
    f.close()
    return d

# функція, яка записує словник у файл (нічого не повертає)
def write_dict(filename, d):
    f = open(filename, "w", encoding="utf-8")
    for key in d:
        f.write(key + ":" + d[key] + "\n")
    f.close()

d = read_dict("dict.txt")
print("Словник з файла dict.txt:")
for key in d:
    print(key, "-", d[key])

word = input("Введіть нове слово: ")
translation = input("Введіть переклад: ")
d[word] = translation

write_dict("dict_new.txt", d)
print("Словник записано у файл dict_new.txt")
