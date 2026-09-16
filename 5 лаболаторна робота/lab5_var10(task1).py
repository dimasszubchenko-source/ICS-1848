import math
x = float(input("Введіть значення x: "))
if x > 0.53:
  
    if (x + 2) != 0:
        f_x = 3 - 0.127 * x + math.log(abs(x + 2))
        print(f"f({x}) = {f_x}")
    else:
        print("Помилка: вираз під логарифмом дорівнює нулю!")

elif -1.2 < x <= 0.53:
    f_x = 2.35 * math.exp(4 * x - 1) + math.cos(x)
    print(f"f({x}) = {f_x}")

else:

  
    if x >= 0:
        f_x = 0.11 * math.sqrt(x) + 3 * math.cos(x)
        print(f"f({x}) = {f_x}")
    else:
        print("Обчислення виразу неможливе: від'ємне число під квадратним коренем!")
