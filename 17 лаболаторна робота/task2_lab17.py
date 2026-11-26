import json
import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE, 'digits.json'), encoding='utf-8') as f:
    data = json.load(f)

s1 = pd.Series(data['first'])
s2 = pd.Series(data['second'])

only1 = s1[~s1.isin(s2)]
only2 = s2[~s2.isin(s1)]
uniq = pd.Series(list(only1) + list(only2))

print('Елементи, які зустрічаються лише в одному масиві:')
print(uniq)
print('Кількість:', len(uniq))

uniq.to_json(os.path.join(BASE, 'uniq.json'), indent=4)
