from array import *
import random

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

masiv = array('i', [0] * 10)
for i in range(10):
    masiv[i] = random.randint(a, b)
print("Вихідний масив:", masiv)

i = 0
while i < len(masiv):
    if masiv.count(masiv[i]) > 1:
        j = i + 1
        while j < len(masiv):
            if masiv[j] == masiv[i]:
                masiv.pop(j)
            else:
                j += 1
    i += 1

print("Масив без повторень:", masiv)
