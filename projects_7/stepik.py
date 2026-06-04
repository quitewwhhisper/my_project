import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 100)  # 100 точек от 0 до 10
y = np.sin(x)                # вычисляем синус для каждой точки
plt.plot(x, y)
plt.show()

