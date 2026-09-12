import math

# Опис функції для обчислення виразу
def calculate_X(a, b, c, x):
    # Косинус у math.cos() приймає радіани
    корінь = math.sqrt(a * math.cos(b) + math.exp(c))
    логарифм = math.log(2**x + 4, 7)
    
    result = корінь + логарифм
    return result

# Введення змінних з клавіатури
a_val = float(input("Введіть a: "))
b_val = float(input("Введіть b (в радіанах): "))
c_val = float(input("Введіть c: "))
x_val = float(input("Введіть x: "))

# Виклик функції та виведення результату
X = calculate_X(a_val, b_val, c_val, x_val)
print(f"Результат X = {X}")
