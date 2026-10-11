n = int(input("Введіть кількість слів N: "))

words = []
for i in range(n):
    word = input("Слово " + str(i + 1) + ": ").strip()
    words.append(word)

counts = {}
for w in words:
    if w != "":
        first = w[0].lower()
        if first in counts:
            counts[first] += 1
        else:
            counts[first] = 1

print("Результат:")
total = 0
for symbol in counts:
    if counts[symbol] > 1:
        print("На літеру '" + symbol + "' починається слів:", counts[symbol])
        total += counts[symbol]

if total == 0:
    print("Слів, що починаються з однакових символів, немає")
else:
    print("Всього слів з однаковими початковими символами:", total)
