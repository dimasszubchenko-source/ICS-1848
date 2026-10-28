import json

# зчитуємо словник з файла JSON
f = open("capitals.json", "r", encoding="utf-8")
data = json.load(f)
f.close()

def save():
    f = open("capitals.json", "w", encoding="utf-8")
    json.dump(data, f, ensure_ascii=False, indent=4)
    f.close()

while True:
    print("1-додати 2-країна 3-столиця 4-видалити 5-всі 0-вихід")
    choice = input("Ваш вибір: ")
    if choice == "1":
        country = input("Введіть країну: ")
        capital = input("Введіть столицю: ")
        data[country] = capital
        save()
        print("Запис додано")
    elif choice == "2":
        country = input("Введіть країну: ")
        if country in data:
            print("Столиця:", data[country])
        else:
            print("Такої країни немає в словнику")
    elif choice == "3":
        capital = input("Введіть столицю: ")
        found = False
        for country in data:
            if data[country] == capital:
                print("Країна:", country)
                found = True
        if not found:
            print("Такої столиці немає в словнику")
    elif choice == "4":
        country = input("Яку країну видалити: ")
        if country in data:
            del data[country]
            save()
            print("Запис видалено")
        else:
            print("Такої країни немає в словнику")
    elif choice == "5":
        for country in data:
            print(country, "-", data[country])
    elif choice == "0":
        print("Роботу завершено")
        break
    else:
        print("Невірний вибір")
