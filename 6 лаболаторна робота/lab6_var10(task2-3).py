import math


a = float(input("Введіть початок діапазону a: "))
b = float(input("Введіть кінець діапазону b: "))
h = float(input("Введіть крок h: "))


f_values = []

print("\n--- Табулювання за допомогою циклу WHILE ---")
x = a

while x <= b + 1e-9:
    denominator = math.pow(2, x) + math.exp(x)
    
    if denominator != 0:
        f_x = x / denominator
        print(f"x = {x:6.2f} | f(x) = {f_x:.6f}")
        
        f_values.append(f_x)
    else:
        print(f"x = {x:6.2f} | Помилка: ділення на нуль!")
        
    x += h


print("\nНесортований список значень функції:")
for val in f_values:
    print(f"{val:.6f}", end=" ")
print()


sorted_values = f_values.copy()

sorted_values.sort(reverse=True)


print("\nВідсортований за спаданням список значень функції:")
for val in sorted_values:
    print(f"{val:.6f}", end=" ")
print()
