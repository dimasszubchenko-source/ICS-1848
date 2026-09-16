import math


a = float(input("Введіть початок діапазону a: "))
b = float(input("Введіть кінець діапазону b: "))
h = float(input("Введіть крок h: "))


n = int((b - a) / h) + 1

print("\n--- Табулювання за допомогою циклу FOR ---")
x = a
for i in range(n):
   
    denominator = math.pow(2, x) + math.exp(x)
    
    if denominator != 0:
        f_x = x / denominator
        print(f"i = {i:2d} | x = {x:6.2f} | f(x) = {f_x:.6f}")
    else:
        print(f"i = {i:2d} | x = {x:6.2f} | Помилка: ділення на нуль!")
        
    x += h
