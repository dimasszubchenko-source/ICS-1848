import math

# площа поверхні піраміди (основа - прямокутник a x b, висота h)
def surface_area(a, b, h):
    h1 = math.sqrt(h ** 2 + (b / 2) ** 2)
    h2 = math.sqrt(h ** 2 + (a / 2) ** 2)
    s_base = a * b
    s_side = a * h1 + b * h2
    return s_base + s_side

# об'єм піраміди
def volume(a, b, h):
    return a * b * h / 3
