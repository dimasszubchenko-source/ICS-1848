import pyramid

a = float(input("Введіть сторону основи a: "))
b = float(input("Введіть сторону основи b: "))
h = float(input("Введіть висоту піраміди h: "))

s = pyramid.surface_area(a, b, h)
v = pyramid.volume(a, b, h)

print("Площа поверхні S =", round(s, 2))
print("Об'єм V =", round(v, 2))
