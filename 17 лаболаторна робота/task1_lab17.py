import os
import pandas as pd

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'start.csv')

df = pd.read_csv(PATH, sep=';', header=None, names=['city1', 'city2'])

df.index = range(1, len(df) + 1)

city1 = df['city1']
city2 = df['city2']

print('Температура в першому місті:')
print(city1)
print()
print('Температура в другому місті:')
print(city2)
