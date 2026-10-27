import random

A = set(random.sample(range(1, 501), 100))
print("Множина A:")
print(sorted(A))

text = input("Введіть елементи множини B: ")
B = set(map(int, text.split()))
print("Множина B:")
print(sorted(B))

print("1) Спільні числа для A і B:")
print(sorted(A & B))
print("2) Числа, що є в A, але відсутні в B:")
print(sorted(A - B))
print("3) Числа, що є в B, але відсутні в A:")
print(sorted(B - A))
