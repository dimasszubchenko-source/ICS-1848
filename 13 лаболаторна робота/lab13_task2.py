import random
import pointspace

points = []
for i in range(10):
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    z = random.randint(-10, 10)
    points.append(pointspace.PointSpace(x, y, z))

print("Усі точки:")
for p in points:
    p.DisplayCoord()

print("Точки І октанта:")
for p in points:
    if p.Octant() == 1:
        p.DisplayCoord()

print("Точки ІІІ октанта:")
for p in points:
    if p.Octant() == 3:
        p.DisplayCoord()

# перевіряємо методи Dist і SetCoord
p = points[0]
print("Перша точка:")
p.DisplayCoord()
print("Відстань до центра:", round(p.Dist(), 2))
p.SetCoord(1, 2, 2)
print("Після SetCoord:")
p.DisplayCoord()
print("Відстань до центра:", round(p.Dist(), 2))
