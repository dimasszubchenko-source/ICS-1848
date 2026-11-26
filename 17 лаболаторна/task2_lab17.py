import json
import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))

# читаємо два словники з файла digits.json
with open(os.path.join(BASE, 'digits.json'), encoding='utf-8') as f:
    data = json.load(f)

# 1) зчитуємо дані у два масиви Series
s1 = pd.Series(data['first'])
s2 = pd.Series(data['second'])

# 2) елементи, які є лише в одному з масивів
only1 = s1[~s1.isin(s2)]
only2 = s2[~s2.isin(s1)]
uniq = pd.Series(list(only1) + list(only2))

print('Елементи, які зустрічаються лише в одному масиві:')
print(uniq)
print('Кількість:', len(uniq))

# 3) зберігаємо результат у файл uniq.json
uniq.to_json(os.path.join(BASE, 'uniq.json'), indent=4)
