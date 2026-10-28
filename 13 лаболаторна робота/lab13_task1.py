class SEA:
    def __init__(self, name, ocean, area, depth):
        self.name = name
        self.ocean = ocean
        self.area = area
        self.depth = depth

    def set_area(self, area):
        self.area = area

    def set_depth(self, depth):
        self.depth = depth

def show(seas):
    for s in seas:
        print(s.name, "|", s.ocean, "|", s.area, "км2 |", s.depth, "м")

seas = [SEA("Чорне", "Атлантичний", 436000, 2212),
        SEA("Середземне", "Атлантичний", 2500000, 5267),
        SEA("Балтійське", "Атлантичний", 415000, 459),
        SEA("Японське", "Тихий", 978000, 3742),
        SEA("Червоне", "Індійський", 438000, 3039)]

print("Список морів:")
show(seas)

name = input("Введіть назву моря для зміни: ")
for s in seas:
    if s.name == name:
        s.set_area(int(input("Нова площа (км2): ")))
        s.set_depth(int(input("Нова глибина (м): ")))

print("Список після змін:")
show(seas)

deepest = seas[0]
for s in seas:
    if s.depth > deepest.depth:
        deepest = s
print("Найглибше море:", deepest.name)
