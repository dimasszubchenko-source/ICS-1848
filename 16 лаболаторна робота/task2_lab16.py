import os
import pylab

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'countries.txt')

names = []
areas = []
with open(PATH, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            name, area = line.rsplit(':', 1)
            names.append(name.strip())
            areas.append(float(area))

x = list(range(len(names)))
pylab.bar(x, areas, color='steelblue')
pylab.xticks(x, names, rotation=45, ha='right')
pylab.ylabel('Площа, км²')
pylab.title('Площі країн')
pylab.tight_layout()
pylab.savefig('countries.png', dpi=200)
pylab.show()
