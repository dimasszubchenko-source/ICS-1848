import random

months = ("січня", "лютого", "березня",
          "квітня", "травня", "червня",
          "липня", "серпня", "вересня",
          "жовтня", "листопада", "грудня")
years = tuple(range(2015, 2026))
days = (31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31)

N = int(input("Введіть N: "))
print("Випадкові дати:")
for i in range(N):
    year = random.choice(years)
    m = random.randint(0, 11)
    max_day = days[m]
    if m == 1 and year % 4 == 0:
        max_day = 29
    day = random.randint(1, max_day)
    print(day, months[m], year)
    