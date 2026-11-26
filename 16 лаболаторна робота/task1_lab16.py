import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 8, 81)
y = 2**x + 3**x


plt.plot(x, y, 'r-', label='y = 2^x + 3^x')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції y = 2^x + 3^x')
plt.grid(True)
plt.legend()


plt.savefig('step.jpg', dpi=300)
plt.show()
