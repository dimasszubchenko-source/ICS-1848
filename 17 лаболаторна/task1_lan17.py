import os
import pandas as pd

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'start.csv')

# зчитуємо файл у DataFrame, дві колонки без заголовка
df = pd.read_csv(PATH, sep=';', header=None, names=['city1', 'city2'])

# індекси від 1 до 7 замість 0..6
df.index = range(1, len(df) + 1)

# два окремі масиви (стовпчики таблиці)
city1 = df['city1']
city2 = df['city2']

print('Температура в першому місті:')
print(city1)
print()
print('Температура в другому місті:')
print(city2)
